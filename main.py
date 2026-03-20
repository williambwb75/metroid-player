# ------------------------- #
# File:     main.py
# Purpose:  open gui
# Python:   3.13.1
# Edited:   3/19/2026
# Author:   williambwb75
# ------------------------- #

import os

from modules.configLoader import configLoader
from modules.shortcutGenerator import generateShortcuts
from modules.emulatorData import generateEmulatorData
from modules.sharedTypes import operatingSystem
from modules.directoryScanner import makeExecutable

def main():
# {
    config = configLoader("config\\config.json")
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