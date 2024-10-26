import os

from remove_plumbob import remove_plumbob
from remove_shadows import remove_shadows
from replace_lightning import replace_files


def get_valid_game_folder():
    while True:
        game_folder = input("Enter the path to The Sims 4 game folder (including The Sims 4 folder itself): ")
        if os.path.isdir(game_folder):
            return game_folder
        else:
            print(f"Error: Game folder not found at '{game_folder}'. Please try again.")


def get_valid_zip_folder():
    while True:
        zip_folder = input("Enter the path to the folder containing the ZIP archive: ")
        if os.path.isdir(zip_folder):
            return zip_folder
        else:
            print(f"Error: ZIP folder not found at '{zip_folder}'. Please try again.")


def main_menu():
    game_folder = get_valid_game_folder()

    while True:
        print("\nThe Sims 4 Post Update Setup")
        print("1. Update Lighting")
        print("2. Remove Plumbob")
        print("3. Remove Shadows")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == '1':
            zip_folder = get_valid_zip_folder()
            zip_name = input("Enter the name of the ZIP file (without .zip extension): ")
            replace_files(game_folder, zip_folder, zip_name)
        elif choice == '2':
            remove_plumbob(game_folder)
        elif choice == '3':
            remove_shadows(game_folder)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

    input("\nPress Enter to close the program.")


if __name__ == "__main__":
    main_menu()
