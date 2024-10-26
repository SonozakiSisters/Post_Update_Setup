import os


def remove_shadows(game_folder_path):
    """
    Modifies the GraphicsRules.sgr file in the Sims 4 game folder
    to disable shadows by setting 'SsaoEnabled false'.

    :param game_folder_path: The Sims 4 game folder path
    """
    sgr_file_path = os.path.join(game_folder_path, 'Game', 'Bin', 'GraphicsRules.sgr')

    # Check if GraphicsRules.sgr exists
    if not os.path.isfile(sgr_file_path):
        print(f"Error: 'GraphicsRules.sgr' not found in the expected location: {sgr_file_path}.")
        return

    # Read the file and modify SsaoEnabled setting
    with open(sgr_file_path, 'r') as file:
        lines = file.readlines()

    # Replace 'SsaoEnabled true' with 'SsaoEnabled false'
    updated_lines = [line.replace('SsaoEnabled true', 'SsaoEnabled false') for line in lines]

    # Write the modified content back to the file
    with open(sgr_file_path, 'w') as file:
        file.writelines(updated_lines)

    print("Shadows removal completed successfully.")
