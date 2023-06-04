# ✔ReMarks!

Remarks app made with Python using _flet_ module.

## Create python virtual environment

First make sure you have installed _virtualenv_:

```bash
pip install virtualenv
```

To use venv in your project, in your terminal, create a new project folder, cd to the project folder in your terminal, and run the following command:

```bash
python<version> -m venv <virtual-environment-name>
```

Example:

```bash
mkdir remarksApp
cd remarksApp
python3.8 -m venv env
```

Python virtual environment created!✨

> _Notes:_
>
> - In this project `<virtual-environment-name>` is called _venv_, so you can call it however you want!
> - Also, python interpreter version used was Python 3.9.0!

## Clone the repo

First clone the repository in a new folder or in `remarksApp` folder created before then create there the virtual environment so the structure would look like this:

├── remarksApp
    ├── `build`
    │   ├── remarks.pkg
    │   ├── remarks.exe.manifest
    │   ├── ...
    ├── `dist`
    │   ├── remarks.exe   
    ├── `venv`
    │   ├── Include
    │   ├── Lib
    │   │   ├── site-packages
    │   ├── Scripts
    │   │   ├── activate.bat
    │   │   ├── ...
    │   ├── pyvenv.cfg  
    ├── `README.md` ----------> This file
    ├── `icon.png`
    ├── `requirements.txt`
    ├── `remarks.py` 
    └── `.gitignore`

## Activate python virtual environment

To activate the venv go to root folder of the project and run the activation script created before:

```bash
remarksApp\venv\Scripts>activate.bat
```

Now in the terminal it should show the activated virtual environment:

```bash
(venv) D:\projects\remarksApp>
```

or

```bash
(venv) D:\projects\remarksApp\venv\Scripts>
```

## Install needed packages

Install needed packages for the project using the _requirements.txt_ file:

```bash
pip install -r requirements.txt
```

All should be done and good to go!

## Check if the app is working

You can run the main script `remarks.py` to check if the app runs or you can run _flet_ with hot reload on a development environment:

```bash
flet `run` remarks.py
```

After running this, the app should open and it should reload it every time you save the changes done to the script `remarks.py` _(development environment)_

## Create a windows application

You can compile an executable `.exe` using _flet_ by using the following command:

```bash
flet `pack` <script-name.py>
```

It can take multiple optional arguments also:

```bash
 (venv) D:\projects\remarksApp>flet pack --help
usage: flet pack [-h] [-v] [-i ICON] [-n NAME] [-D] [--distpath DISTPATH] [--add-data [ADD_DATA ...]]
                 [--hidden-import [HIDDEN_IMPORT ...]] [--product-name PRODUCT_NAME]
                 [--file-description FILE_DESCRIPTION] [--product-version PRODUCT_VERSION]
                 [--file-version FILE_VERSION] [--company-name COMPANY_NAME] [--copyright COPYRIGHT]
                 [--bundle-id BUNDLE_ID]
                 script

Package Flet app to a standalone bundle

positional arguments:
  script                path to a Python script

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         -v for detailed output and -vv for more detailed
  -i ICON, --icon ICON  path to an icon file (.ico, .png, .icns)
  -n NAME, --name NAME  name for the generated executable (Windows) or app bundle (macOS)
  -D, --onedir          create a one-folder bundle containing an executable (Windows)
  --distpath DISTPATH   where to put the bundled app (default: ./dist)
  --add-data [ADD_DATA ...]
                        additional non-binary files or folders to be added to the executable
  --hidden-import [HIDDEN_IMPORT ...]
                        add an import not visible in the code of the script(s)
  --product-name PRODUCT_NAME
                        executable product name (Windows) or bundle name (macOS)
  --file-description FILE_DESCRIPTION
                        executable file description (Windows)
  --product-version PRODUCT_VERSION
                        executable product version (Windows) or bundle version (macOS)
  --file-version FILE_VERSION
                        executable file version, n.n.n.n (Windows)
  --company-name COMPANY_NAME
                        executable company name (Windows)
  --copyright COPYRIGHT
                        executable (Windows) or bundle (macOS) copyright
  --bundle-id BUNDLE_ID
                        bundle identifier (macOS)
```

For example to create an executable that also has a custom icon we can pass `--icon` argument like so:

```bash
flet pack --icon icon.png remarks.py
```

This will use `pyinstaller` to create the application and it will be found in the root folder in the `dist` directory created by `pyinstaller` as **`remarks.exe`**

DONE! 🎉
