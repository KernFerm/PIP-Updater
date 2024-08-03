# PIP Updater

PIP Updater is a Python script designed to automatically upgrade all installed pip packages on a system. It simplifies the process of keeping Python packages up-to-date by iterating over all installed packages and upgrading them to their latest versions.

## how to download the repo first time users

  - click link to read [**Instructions**](https://www.gitprojects.fnbubbles420.org/how-to-download-repos)

## Features

- Automatically upgrades all installed pip packages.
- Utilizes the `pkg_resources` module to list installed packages.
- Uses the `subprocess` module to execute pip commands.
- Prints out a log file of all the current updated packages that got updated.


## Getting Started

### Dependencies

- Python 3.11.6 included   ( `adds python.exe to path automatically` )
        [Python 3.11.6 auto installer](https://github.com/KernFerm/PIP-Updater/blob/main/py3.11.6_Installer.bat)
- pip

### Installing

- Clone this repository or download the `main.py` file.
- Ensure Python and pip are installed on your system.

### Executing program

- Run the script using Python:

```bash
python main.py
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- This script was created to simplify the maintenance of Python environments, making it easier for developers to keep their packages up-to-date.
