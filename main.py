# ------------------------- #
# File:     main.py
# Purpose:  open gui
# Python:   3.13.1
# Edited:   3/19/2026
# Author:   williambwb75
# ------------------------- #

import os

from configLoader import configLoader
from shortcutGenerator import generateShortcuts
from emulatorData import generateEmulatorData
from sharedTypes import operatingSystem
from directoryScanner import makeExecutable

def main():
# {
    config = configLoader("config.json")
    generateEmulatorData(config.operatingSystem)
    generateShortcuts(config.romFolders, config.operatingSystem, config.outputFolder)
    if (config.operatingSystem == operatingSystem.LINUX):
    # {
        makeExecutable(config.outputFolder)
    # }
    return 0
# }

if __name__ == "__main__":
# {
    main()
# }