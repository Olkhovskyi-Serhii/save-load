import os
import json
from pathlib import Path

def find_project_root(marker_file='main.py'):
    """
    Searches for the project root directory using a marker file.

    Traverses upward through the directory tree until the specified file is found.
    Used to construct absolute paths relative to the project root.

    Args:
        marker_file (str): The name of the file that identifies the project root.

    Returns:
        Path: Path to the project's root directory.

    Raises:
        FileNotFoundError: If the marker file is not found in the directory hierarchy.

    """
    current_dir = Path(__file__).resolve().parent

    while not (current_dir / marker_file).exists():

        if current_dir.parent == current_dir:
            raise FileNotFoundError(f"Не удалось найти корень проекта с маркером '{marker_file}'.")
        current_dir = current_dir.parent

    return current_dir

def save_json(data, file_name, relative_path=None):
    """
    Saves data to a JSON file at a custom path relative to the project root.

    Args:
        data (list | dict): The data to be saved.
        file_name (str): Name of the JSON file.
        relative_path (str | None): Custom path relative to project root.
                                    Example: "data/files_json/db_json"
                                    If None, saves directly in project root.

    Returns:
        None
    """

    base_path = find_project_root()

    if relative_path:
        base_path = base_path / relative_path

    file_path = base_path / file_name

    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_json(file_name, relative_path=None):
    """
    Loads JSON data from a custom path relative to the project root.

    Args:
        file_name (str): Name of the JSON file.
        relative_path (str | None): Custom path relative to project root.
                                    Example: "data/files_json/db_json"
                                    If None, loads directly from project root.

    Returns:
        Any: Loaded JSON data (list, dict, etc.)

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
    """

    base_path = find_project_root()

    if relative_path:
        base_path = base_path / relative_path

    file_path = base_path / file_name

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)