# Car Race Project [![Python Tests](https://github.com/babutabhavya/CarRaceProject/actions/workflows/python.yml/badge.svg)](https://github.com/babutabhavya/CarRaceProject/actions/workflows/python.yml)

#### ***Advanced Programming Project, Masters of Computer Science, SRH, Berlin School of Technology***

## Team Member Details:
1.  Bhavya Babuta - 3120456
2.  Deepshikha - 3118045
3.  Francisco Saavedra Gonzalez - 3121202

## Table of Contents

- [Prerequisites](#prerequisites)
- [Makefile commands](#makefile-commands)

## Prerequisites

Before running the build management commands, make sure you have the following installed on your system:

- **Python:** The project uses Python, and you can install it from [python.org](https://www.python.org/).
- **Pip:** Pip is the package installer for Python. You can check if you have it installed by running `pip --version`. If not, you can install it using the instructions on the [official Pip website](https://pip.pypa.io/en/stable/installation/).
- **Pipenv:** Pipenv is used for virtual environment management. You can install it using `pip install pipenv`.
- **Makefile:** The build management commands are defined in the Makefile. Make sure you have `make` installed on your system. On Linux, you can typically install it with `sudo apt-get install make`, and on macOS, it comes pre-installed. Installing Make for Windows, follow the following steps

1. **Download Make for Windows:**
   - Visit the [GNU Make official website](http://gnuwin32.sourceforge.net/packages/make.htm).
   - Scroll down to the "Binaries" section.
   - Download the latest complete package, e.g., `Complete package, except sources` by clicking on the link.
   - This will download a ZIP file.

2. **Extract the ZIP file:**
   - Extract the contents of the ZIP file to a directory of your choice.

3. **Add Make to System Path:**
   - After extracting, add the path to the Make executable to your system's PATH environment variable.
     - Right-click on "This PC" or "My Computer" and select "Properties."
     - Click on "Advanced system settings" on the left.
     - Click on the "Environment Variables" button.
     - In the "System variables" section, find the "Path" variable, select it, and click "Edit."
     - Click "New" and add the path to the directory containing the `make.exe` executable.

4. **Verify Installation:**
   - Open a new command prompt or PowerShell window.
   - Type `make --version` and press Enter. You should see the Make version information if the installation was successful.

Now you should have Make installed on your Windows system. You can proceed with the build management commands using Make.


## Makefile commands

- **`makemigrations`**: Create database migration files for changes in models.
- **`migrate`**: Apply database migrations to update the database schema.
- **`run`**: Start the Django development server to run the application.
- **`setup`**: Install project dependencies, including development dependencies.
- **`check-format`**: Check code formatting using Black without making changes.
- **`format`**: Format code using Black to adhere to the specified style.
- **`check-import-order`**: Check import order using isort with a profile for Black.
- **`import-order`**: Organize import order using isort with a profile for Black.
- **`lint`**: Run pylint to perform static code analysis on the project.
- **`check`**: Check code formatting, import order, and linting.
- **`test`**: Run pytest to execute all tests in the project with coverage.
- **`help`**: Display a help message with available Makefile targets and their explanations.

## Design Patterns

- [Factory](https://github.com/Deepshikha1611/CarRaceProject/blob/main/src/components/animations/main.py)
- [Abstract](https://github.com/Deepshikha1611/CarRaceProject/blob/main/src/base/car.py)


## Checklists

- [x] The game is working
- [x] There is a Git repository
- [x] There is a README file including installation instructions
- [x] There is a requirements.txt or pyproject.toml file
- [x] No function is longer than 20 lines
- [x] There is at least one class with 3+ attributes and 3+ methods
- [x] There is a class diagram, sequence diagram, state diagram, or other type of design diagram
- [x] There are 3+ automated tests that pass
- [x] The project uses Continuous Integration
- [x] Python style checks pass
- [x] The project is pip-installable
- [x] The game contains custom graphics
- [x] The game contains sound effects and/or music
- [x] Great gameplay (up to 2 points)

## Game play instructions :car:

-Use the following keys to play the game

- W-forward
- A-turn left
- S-brake or move backward
- D-right

## References

- The code was developed using the [Pygame Car Racing Tutorial by TechWithTim](https://www.youtube.com/watch?v=L3ktUWfAMPg&t=2292s)
- The GIF Images are used from https://tenor.com/view/
- [Winning Gif](https://tenor.com/view/wow-winning-race-car-racing-car-racer-gif-15169358), [Losing Gif](https://tenor.com/view/out-of-control-motorsports-on-nbc-nascar-on-nbc-lose-control-drifting-gif-18116496)
- [Background image](https://www.istockphoto.com/de/vektor/textur-von-gr%C3%BCnem-gras-auf-dem-fu%C3%9Fballplatz-gm1397509122-451918466mediatype=illustration&phrase=grass+top+view)
- [Trees added to the background with photosho](https://pngtree.com/freepng/green-cartoon-forest-material-big-tree-illustration-tree-clipart_5563889.html)
- [Car obtained from and resized pixels and color edited with photoshop](https://pngtree.com/freepng/cool-sports-car-top-view-vector_9068335.html)
- [The track was obtained from and borders edited with photoshop](https://www.pngwing.com/en/free-png-hvbdh)
- The sound are used from https://pixabay.com/sound-effects/
- [Acceleration Sound](https://pixabay.com/sound-effects/car-acceleration-inside-car-7087/)
- [Losing Sound](https://pixabay.com/sound-effects/8-bit-video-game-fail-version-2-145478/)
- [Winning Sound](https://pixabay.com/sound-effects/crowd-cheering-143103/)
