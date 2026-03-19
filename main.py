# ------------------------- #
# File:     main.py
# Purpose:  open gui
# Python:   3.13.1
# Edited:   3/19/2026
# Author:   williambwb75
# ------------------------- #

from modules.configLoader import configLoader
from modules.shortcutGenerator import generateShortcuts
from modules.emulatorData import generateEmulatorData

def main():
# {
    config = configLoader("config\\config.json")
    generateEmulatorData(config.operatingSystem)
    generateShortcuts(config.romFolders, config.operatingSystem, config.outputFolder)
    return 0
# }

if __name__ == "__main__":
# {
    main()
# }