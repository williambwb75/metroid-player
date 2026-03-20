# ------------------------- #
# File:     shortcutGenerator.py
# Purpose:  generate shortcuts
# Python:   3.13.1
# Edited:   3/19/2026
# Author:   williambwb75
# ------------------------- #

import os

from directoryScanner import directoryScanner
from sharedTypes import operatingSystem, romType
import emulatorData as emulator

class romFolder:
# {
    def __init__(self, romType, path):
    # {
        self.romType = romType
        self.romPath = path
    # }
# }

def createShortcut(p_operatingSystem, command, name, outputFolder):
# {
    if p_operatingSystem == operatingSystem.LINUX:
    # {
        with open(outputFolder + "/" + name + ".desktop", "w") as f:
        # {
            f.write("[Desktop Entry]\n")
            f.write("Type=Application\n")
            f.write("Name=" + name + "\n")
            f.write("Exec=" + command + "\n")
            f.write("Icon=application-x-executable\n")
            f.write("Terminal=false\n")
        # }
    # }
    elif p_operatingSystem == operatingSystem.WINDOWS:
    # {
        with open(outputFolder + "\\" + name + ".bat", "w") as f:
        # {
            f.write(command)
        # }
    # }
    else:
    # {
        raise ValueError("Unsupported operating system")
# }

def generateShortcuts(romFolders, operatingSystem, outputFolder):
# {
    os.makedirs(outputFolder, exist_ok=True)
    SYSTEMS = \
    {
        romType.NES:       ("nes",       emulator.Nestopia,  ".nes"),
        romType.SNES:      ("snes",      emulator.SNES9x,    ".sfc"),
        romType.GBA:       ("gba",       emulator.mGBA,      ".gba"),
        romType.WII:       ("wii",       emulator.Dolphin,   ".iso"),
        romType.PRIMEHACK: ("primehack", emulator.PrimeHack, ".iso"),
        romType._3DS:      ("3ds",       emulator.Azahar,    ".cci"),
    }
    for romFolder in romFolders:
    # {
        folderName, emulatorObj, extension = SYSTEMS[romFolder.romType]
        systemOutput = os.path.join(outputFolder, folderName)
        os.makedirs(systemOutput, exist_ok=True)
        for rom in directoryScanner(romFolder.romPath):
        # {
            romPath = os.path.join(romFolder.romPath, rom)
            shortcutCommand = emulatorObj.createShortcutCommand(romPath)

            romName = rom[:-len(extension)] if rom.endswith(extension) else rom
            createShortcut(operatingSystem, shortcutCommand, romName, systemOutput)
        # }
    # }
# }