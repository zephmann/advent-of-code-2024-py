
import os


def get_input_file(module_file_path):
    """Return the corresponding input text file path for a day python module."""
    src_dir, input_file = os.path.split(module_file_path)
    project_dir = os.path.dirname(os.path.dirname(src_dir))
    input_file = os.path.splitext(input_file)[0] + ".txt"
    input_file = os.path.join(project_dir, "input", input_file)
    print(f"Input file: {input_file}")
    return os.path.join(project_dir, "input", input_file)
