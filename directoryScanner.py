# ------------------------- #
# File:     directoryScanner.py
# Purpose:  open gui
# Python:   3.13.1
# Edited:   3/19/2026
# Author:   williambwb75
# ------------------------- #

import os

def directoryScanner(path):
# {
    return os.listdir(path)
# }

def makeExecutable(path):
# {
    for folder in directoryScanner(path):
    # {
        for file in directoryScanner(f"{path}\\{folder}"):
        # {
            if (file.endswith(".desktop")):
            # {
                os.system(f"chmod +x {path}\\{folder}\\{file}")
            # }
        # }
    # }
# }