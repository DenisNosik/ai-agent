import os
import subprocess
from google.genai import types


def run_python_file(working_directory, file_path, args=None):
    try:
        abs_working_dir  = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))
        valid_target_file = os.path.commonpath([abs_working_dir, target_file]) == abs_working_dir

        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_file]
        
        if args:
            command.extend(args)
        
        completed_process = subprocess.run(command, cwd=abs_working_dir, capture_output=True, text=True, timeout=30)    
        output = []
        
        if completed_process.returncode != 0:
            output.append(f"Process exited with code {completed_process.returncode}")
        if not completed_process.stdout and not completed_process.stderr:
            output.append(f"No output produced")
        if completed_process.stdout:
            output.append(f"STDOUT:\n{completed_process.stdout}")
        if completed_process.stderr:
            output.append(f"STDERR:\n{completed_process.stderr}")
        
        return "\n".join(output)
    
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run python file from a specified file path",
    parameters=types.Schema(
        required=["file_path"],
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="file path to list file from, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="list of arguments for command subprocess",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
    ),
)