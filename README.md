AI File Agent (Python)

An experimental AI-powered agent that can interact with files inside a working directory (default is "calculator/").
The agent can read, write, and execute code, analyze results, and iteratively improve files based on feedback.

It is powered by Gemini 2.5 Flash and works as a lightweight local development assistant.

Requirements
Python 3
Gemini API key

This project uses Gemini 2.5 Flash.
You must create your own API key

For safety:
Run it inside a sandboxed directory
Do not use it on important system folders

Example task for the agent:
uv run main.py "what's in main.py file?"

The agent will:
get file from working directory (calculator/main.py)
explain what is in that file


