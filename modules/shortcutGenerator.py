# ------------------------- #
# File:     shortcutGenerator.py
# Purpose:  generate shortcuts
# Python:   3.13.1
# Edited:   3/19/2026
# Author:   williambwb75
# ------------------------- #

import os

from modules.directoryScanner import directoryScanner
from modules.sharedTypes import operatingSystem, romType
import modules.emulatorData as emulator

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
    if (os.path.exists(outputFolder) == False): os.mkdir(outputFolder)
    for romFolder in romFolders:
    # {
        if romFolder.romType == romType.NES:
        # {
            if (os.path.exists(outputFolder + "\\" + "nes") == False): os.mkdir(outputFolder + "\\" + "nes")
            for rom in directoryScanner(romFolder.romPath):
            # {
                shortcutCommand = emulator.Nestopia.createShortcutCommand(romFolder.romPath + "\\" + rom)
                createShortcut(operatingSystem, shortcutCommand, rom.rstrip(".nes"), outputFolder+"\\"+"nes")
            # }
        # }
        elif romFolder.romType == romType.SNES:
        # {
            if (os.path.exists(outputFolder + "\\" + "snes") == False): os.mkdir(outputFolder + "\\" + "snes")
            for rom in directoryScanner(romFolder.romPath):
            # {
                shortcutCommand = emulator.SNES9x.createShortcutCommand(romFolder.romPath + "\\" + rom)
                createShortcut(operatingSystem, shortcutCommand, rom.rstrip(".sfc"), outputFolder+"\\"+"snes")
            # }
        # }
        elif romFolder.romType == romType.GBA:
        # {
            if (os.path.exists(outputFolder + "\\" + "gba") == False): os.mkdir(outputFolder + "\\" + "gba")
            for rom in directoryScanner(romFolder.romPath):
            # {
                shortcutCommand = emulator.mGBA.createShortcutCommand(romFolder.romPath + "\\" + rom)
                createShortcut(operatingSystem, shortcutCommand, rom.rstrip(".gba"), outputFolder+"\\"+"gba")
            # }
        # }
        elif romFolder.romType == romType.WII:
        # {
            if (os.path.exists(outputFolder + "\\" + "wii") == False): os.mkdir(outputFolder + "\\" + "wii")
            for rom in directoryScanner(romFolder.romPath):
            # {
                shortcutCommand = emulator.Dolphin.createShortcutCommand(romFolder.romPath + "\\" + rom)
                createShortcut(operatingSystem, shortcutCommand, rom.rstrip(".iso"), outputFolder+"\\"+"wii")
            # }
        # }
        elif romFolder.romType == romType.PRIMEHACK:
        # {
            if (os.path.exists(outputFolder + "\\" + "primehack") == False): os.mkdir(outputFolder + "\\" + "primehack")
            for rom in directoryScanner(romFolder.romPath):
            # {
                shortcutCommand = emulator.PrimeHack.createShortcutCommand(romFolder.romPath + "\\" + rom)
                createShortcut(operatingSystem, shortcutCommand, rom.rstrip(".iso"), outputFolder+"\\"+"primehack")
            # }
        # }
        elif romFolder.romType == romType._3DS:
        # {
            if (os.path.exists(outputFolder + "\\" + "3ds") == False): os.mkdir(outputFolder + "\\" + "3ds")
            for rom in directoryScanner(romFolder.romPath):
            # {
                shortcutCommand = emulator.Azahar.createShortcutCommand(romFolder.romPath + "\\" + rom)
                createShortcut(operatingSystem, shortcutCommand, rom.rstrip(".cci"), outputFolder+"\\"+"3ds")
            # }
        # }
    # }
# }