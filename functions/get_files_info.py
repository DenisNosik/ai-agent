import os

def get_files_info(working_directory, directory="."):
    try:
        abs_working_dir  = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))
        valid_target_dir = os.path.commonpath([abs_working_dir, target_dir]) == abs_working_dir
        valid_dir = os.path.isdir(target_dir)
        return_data_list = []

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not valid_dir:
            return f'Error: "{directory}" is not a directory'
        
        for item in os.listdir(target_dir):
            return_data_list.append(f'- {item}: file_size={os.path.getsize(target_dir + "/" + item)} bytes, is_dir={os.path.isdir(target_dir + "/" + item)}')
        
        return "\n".join(return_data_list)
    except Exception as e:
        return f"Error listing files: {e}"