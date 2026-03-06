import os
import argparse
from config import MAX_ITERATIONS
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from functions.call_function import available_functions, call_function


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        raise RuntimeError("API Key Not Found")
    
    client = genai.Client(api_key=api_key)
    
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    for _ in range(20):
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash', 
                contents=messages,
                config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
            )

            if response.usage_metadata == None:
                raise RuntimeError("Failed API request")

            if args.verbose:
                print(f"User prompt: {args.user_prompt}")
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

            conversation_history = response.candidates
            
            if len(conversation_history) > 0:
                for candidat in conversation_history:
                    messages.append(candidat.content)

            function_calls = response.function_calls
            function_results = []

            if function_calls != None:
                for function_call in function_calls:
                    function_call_result = call_function(function_call)
                    if len(function_call_result.parts) == 0:
                        raise Exception("ERROR: List of parts is empty")
                    if function_call_result.parts[0].function_response == None:
                        raise Exception("ERROR: Function Response is NONE")
                    if function_call_result.parts[0].function_response.response == None:
                        raise Exception("ERROR: Function Response .response is NONE")
                    
                    function_results.append(function_call_result.parts[0])

                    if args.verbose:
                        print(f"-> {function_call_result.parts[0].function_response.response}")
                
                messages.append(types.Content(role="user", parts=function_results))

            else:
                print("Final response:")
                print(response.text)
                return

        except Exception as e:
            print(f"ERROR: {e}")
    print(f"Maximum interations ({MAX_ITERATIONS}) reached")
        
        


if __name__ == "__main__":
    main()
