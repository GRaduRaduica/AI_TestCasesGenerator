"""
Short script to find all the dirs and files from current py project
"""

from pathlib import Path

current_file_path = Path(__file__).resolve()
current_dir_path = current_file_path.parent


def find_file(target_file):
    """
    Recursively search for a file with the exact name within current_dir_path and its subdirectories.
    :param target_file: file name (e.g., 'data.json')
    :return: full path of the first match, or None
    """
    for file in current_dir_path.rglob(target_file):
        if file.is_file():
            return file
    return None


def find_dir(dir_target):
    """
    Returns directory path
    :param dir_target: name of the directory
    :return: full path of dir_target
    """
    for dir in current_dir_path.iterdir():
        if dir.is_dir() and dir.name == dir_target:
            return dir
    return None


# if __name__ == '__main__':
#     print(find_dir('../excel_input'))
#     print(find_file("dummy_sample.xlsx"))