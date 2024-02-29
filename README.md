# Car Race Project

#### ***Advanced Programming Project, Masters of Computer Science, student at SRH, Berlin School of Technology***

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

