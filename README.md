# Post Update Setup for The Sims 4

A Python application to perform post setup tasks, i.e. remove plumbob, shadows and update the  lightning.

## Prerequisites

To run this project locally, you need the following:

- Python 3.7+
- Pip (if you want to generate exe file)


## Setup Instructions

### 1. Clone the Repository
Clone the project to your local machine:

    git clone https://github.com/yourusername/SonozakiSisters_Post_Update_Setup.git

### 2. Install Required Dependencies
Use pip to install the required dependencies:

    pip install -r requirements.txt

###3. Run the Project Locally
To run the project locally, execute the main script:

    python main.py

## Usage

Input The Sims 4 folder path (including the folder itself) to proceed.

### Available menu options

#### Update Lighting:

Enter path to custom lightning ZIP archive, and it's name without .zip extension

This option updates in game lightning files (in Data and Delta folders) with archived files. 

#### Remove Plumbob:

Edits the Default.ini file in the game directory to hide Plumbob.

#### Remove Shadows:

Edits the GraphicsRules.sgr file in the game directory to disable game shadows.

#### Exit:
Ends the program.

## Building the Executable

If you want to create a standalone executable for the project, run the following command:

    pyinstaller --onefile --name SonozakiSisters_Post_Update_Setup --icon icon.ico main.py

After building, the executable will be located in the dist folder.

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any improvements or bug fixes.