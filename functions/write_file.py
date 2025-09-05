import os
from google.genai import types


def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: {file_path} is not in the working directory'

    parent_dir = os.path.dirname(abs_file_path)
    if not os.path.isdir(parent_dir):
        try:
            os.makedirs(parent_dir)
        except Exception as e:
            return f'Could not create the parent directory: {parent_dir} = {e}'
    try:
        with open(abs_file_path, 'w') as f:
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        return f'Failed to write to {file_path}, {e}'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Overwrites an existing file or writes to a new file if it doesn't exist and creates required parents dirs safely, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to be written.",
            ),
            "contents": types.Schema(
                type=types.Type.STRING,
                description="The contents to write to the file as a string.",
            ),
        },
    ),
)