import os
from google.genai import types


def write_file(working_directory, file_path, content):
    try:
        abs_working_dir  = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))
        valid_target_file = os.path.commonpath([abs_working_dir, target_file]) == abs_working_dir

        if not valid_target_file:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        with open(target_file, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f"Error writing file: {e}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write content to file in a specified directory relative to the working directory",
    parameters=types.Schema(
        required=["file_path", "content"],
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="file path to list file from, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="content that's need to be written to the file"
            )
        },
    ),
)
