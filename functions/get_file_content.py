import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))
        valid_target_file = os.path.commonpath([abs_working_dir, target_file]) == abs_working_dir
        valid_file = os.path.isfile(target_file)

        if not valid_target_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not valid_file:
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(target_file, "r") as f:
            content = f.read(MAX_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        
        return content
    except Exception as e:
        return f"Error listing file: {e}"
        

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="List file content from a specified file path, providing file content",
    parameters=types.Schema(
        required=["file_path"],
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="file path to list file from, relative to the working directory",
            ),
        },
    ),
)
    