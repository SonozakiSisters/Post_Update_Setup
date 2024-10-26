import os


def read_file_lines(file_path):
    """Reads all lines from file."""
    with open(file_path, 'r') as file:
        return file.readlines()


def write_file_lines(file_path, lines):
    """Writes all lines to file."""
    with open(file_path, 'w') as file:
        file.writelines(lines)


def is_plumbob_section_start(line):
    """Checks if the current line is the start of [PlumbBob] section."""
    return line.strip().startswith('[PlumbBob]')


def modify_plumbob_line(line):
    """
    Modifies RGBA values in PlumbBob section line.
    The alpha (last) value is set to 0.00.
    """
    key, value = line.split('=', 1)
    value_parts = value.split(',')

    if len(value_parts) == 4:  # Ensure it's a RGBA line
        value_parts[-1] = ' 0.00'
        updated_value = ','.join(value_parts)
        return f"{key} = {updated_value}\n"

    return line


def update_plumbob_section(lines):
    """
    Updates the PlumbBob section in the list of lines.
    Changes the alpha value in RGBA colors to 0.00.
    """
    updated_lines = []

    for line in lines:
        if is_plumbob_section_start(line):

            if '=' in line.strip():
                updated_lines.append(modify_plumbob_line(line))
            else:
                updated_lines.append(line)
        else:
            updated_lines.append(line)

    return updated_lines


def remove_plumbob(game_folder_path):
    """
    Modifies the Default.ini file in the Bin folder to set PlumbBob RGBA values' alpha to 0.00.

    :param game_folder_path: The root directory of the Sims 4 game folder
    """
    ini_file_path = os.path.join(game_folder_path, 'Game', 'Bin', 'Default.ini')

    if not os.path.isfile(ini_file_path):
        print(f"Error: 'Default.ini' not found in the expected location: {ini_file_path}.")
        return

    lines = read_file_lines(ini_file_path)
    updated_lines = update_plumbob_section(lines)
    write_file_lines(ini_file_path, updated_lines)

    print("Plumbob removal completed successfully.")
