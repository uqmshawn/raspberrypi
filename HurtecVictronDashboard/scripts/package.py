"""Simple packaging script using PyInstaller."""
import os
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

DIST_DIR = ROOT / 'dist'
DIST_DIR.mkdir(exist_ok=True)

PYINSTALLER_CMD = [
    'pyinstaller',
    '--noconfirm',
    '--clean',
    '--onefile',
    '--name', 'hurtec_dashboard',
    str(ROOT / 'src' / 'main.py')
]


def build():
    subprocess.check_call(PYINSTALLER_CMD)
    built = ROOT / 'dist' / ('hurtec_dashboard.exe' if os.name == 'nt' else 'hurtec_dashboard')
    print('Built', built)


if __name__ == '__main__':
    build()
