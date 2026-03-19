# ------------------------- #
# File:     emulatorData.py
# Purpose:  define data structures for emulators
# Python:   3.13.1
# Edited:   3/19/2026
# Author:   williambwb75
# ------------------------- #

mGBA        = None
Dolphin     = None
SNES9x      = None
Azahar      = None
Nestopia    = None
PrimeHack   = None

from modules.sharedTypes import operatingSystem, romType

class emulatorData:
# {
    def __init__(self, name, path, arguments=[]):
    # {
        self.name = name
        self.path = path
        self.arguments = arguments
    # }

    def createShortcutCommand(self, romPath):
    # {
        command = self.path
        for argument in self.arguments: command += " " + f'"argument"'
        command += " " + f'"{romPath}"'
        return command
    # }
# }

def generateEmulatorData(operatingSystem):
# {
    global mGBA     
    global Dolphin  
    global SNES9x   
    global Azahar   
    global Nestopia 
    global PrimeHack

    if operatingSystem == operatingSystem.LINUX:
    # {
        mGBA        = emulatorData("mGBA",      "flatpak run org.mgba.mgba")
        Dolphin     = emulatorData("Dolphin",   "flatpak run org.DolphinEmu.dolphin-emu")
        SNES9x      = emulatorData("SNES9x",    "flatpak run org.snes9x.snes9x")
        Azahar      = emulatorData("Azahar",    "flatpak run org.azahar.azahar")
        Nestopia    = emulatorData("Nestopia",  "flatpak run org.nestopia.nestopia")
        PrimeHack   = emulatorData("PrimeHack", "flatpak run org.primehack.primehack")
    # }
    elif operatingSystem == operatingSystem.WINDOWS:
    # {
        mGBA        = emulatorData("mGBA",      "C:\\Emulators\\mGBA\\mgba.exe")
        Dolphin     = emulatorData("Dolphin",   "C:\\Emulators\\Dolphin\\dolphin.exe")
        SNES9x      = emulatorData("SNES9x",    "C:\\Emulators\\SNES9x\\snes9x.exe")
        Azahar      = emulatorData("Azahar",    "C:\\Emulators\\Azahar\\azahar.exe")
        Nestopia    = emulatorData("Nestopia",  "C:\\Emulators\\Nestopia\\nestopia.exe")
        PrimeHack   = emulatorData("PrimeHack", "C:\\Emulators\\PrimeHack\\primehack.exe")
    # }
    else:
    # {
        raise ValueError("Unsupported operating system")
    # }
# }