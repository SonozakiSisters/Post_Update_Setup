import os
import shutil
import zipfile

VALID_ROOT_DIRS = ['Data', 'Delta']


def extract_zip(zip_file_path, extract_folder):
    """Extracts ZIP file to a temporary folder."""
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)


def find_relevant_path(relative_path):
    """Finds relevant part of the path starting from a valid root directory."""
    path_parts = relative_path.split(os.sep)

    for idx, part in enumerate(path_parts):
        if part in VALID_ROOT_DIRS:
            return os.path.join(*path_parts[idx:])

    return None


def replace_file(source_path, target_path):
    """Replaces target file with source file if exists."""
    if os.path.exists(target_path):
        print(f"Replacing: {target_path}")
        shutil.copy2(source_path, target_path)
    else:
        print(f"Skipping non-existent target: {target_path}")


def clean_up_folder(folder_path):
    """Removes temporary extraction folder."""
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)


def replace_files(game_folder_path, zip_folder_path, zip_name):
    """
    Unzips the given ZIP file and replaces matching game files in the target folder.

    :param game_folder_path: A root directory of the Sims 4 game folder (including The Sims 4 folder itself).
    :param zip_folder_path: A folder containing ZIP archive.
    :param zip_name: ZIP file name (without the .zip extension).
    """
    zip_file_path = os.path.join(zip_folder_path, f"{zip_name}.zip")

    if not os.path.isfile(zip_file_path):
        print(f"Error: ZIP archive '{zip_name}.zip' not found in '{zip_folder_path}'.")
        return

    extract_folder = 'temp_extracted'

    try:
        extract_zip(zip_file_path, extract_folder)

        for root, _, files in os.walk(extract_folder):
            for file in files:
                relative_path = os.path.relpath(os.path.join(root, file), extract_folder)
                relevant_path = find_relevant_path(relative_path)

                if relevant_path:
                    target_path = os.path.join(game_folder_path, relevant_path)
                    replace_file(os.path.join(root, file), target_path)

    finally:
        clean_up_folder(extract_folder)
