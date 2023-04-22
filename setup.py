import sys
from cx_Freeze import setup, Executable

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"

executables = [Executable("autoaccept.py", base=base, icon="icon.ico")]
packages = ["idna", "tkinter", "pyautogui", "os"]
options = {
    'build_exe': {
        'packages': packages,
        'include_files': ['icon.ico', 'config.json', "Languages"]
    },
}

setup(
    name="autoaccept",
    options=options,
    version="1.0",
    description='Queue Accepter',
    executables=executables
)
