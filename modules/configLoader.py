# ------------------------- #
# File:     configLoader.py
# Purpose:  open gui
# Python:   3.13.1
# Edited:   3/19/2026
# Author:   williambwb75
# ------------------------- #

from enum import Enum
import json

from sqlalchemy import case
from modules.directoryScanner import directoryScanner

from tomlkit import key, value

class operatingSystem(Enum):
# {
    LINUX   = 0
    WINDOWS = 1
# }

class romType(Enum):
# {
    NES         = 0
    SNES        = 1
    GBA         = 2
    WII         = 3
    PRIMEHACK   = 4
    _3DS        = 5

# }

class romFolder:
# {
    def __init__(self, romType, path):
    # {
        self.romType = romType
        self.romPath = path
    # }
# }

class configLoader:
# {
    def __init__(self, configFilePath):
    # {
        self.configFilePath = configFilePath
        self.__getOperatingSystem()
        self.__getRomPaths()
    # }

    def __getOperatingSystem(self):
    # {
        try:
        # {
            with open(self.configFilePath) as file:
            # {
                jsonFile = json.load(file)
            # }
            match jsonFile["operatingSystem"]:
            # {
                case "LINUX":   self.operatingSystem = operatingSystem.LINUX
                case "WINDOWS": self.operatingSystem = operatingSystem.WINDOWS
                case _: raise TypeError("invalid value for attribute 'operatingSystem' in config file")
            # }
        # }
        except FileNotFoundError:
        # {
            raise FileNotFoundError("Config file not found:", self.configFilePath)
        # }
        except KeyError:
        # {
            raise KeyError("Missing 'operatingSystem' in config file")
        # }
        except json.JSONDecodeError:
        # {
            raise ValueError("invalid JSON found in config file")
        # }
    # }

    def __getRomPaths(self):
    # {
        try:
        # {
            with open(self.configFilePath) as file:
            # {
                jsonFile = json.load(file)
            # }
            self.romFolders = []
            for folder in directoryScanner(jsonFile["romsFolder"]):
            # {
                match folder.lower():
                # {
                    case "nes":          self.romFolders.append(romFolder(romType.NES,          value))
                    case "snes":         self.romFolders.append(romFolder(romType.SNES,         value))
                    case "gba":          self.romFolders.append(romFolder(romType.GBA,          value))
                    case "wii":          self.romFolders.append(romFolder(romType.WII,          value))
                    case "primehack":    self.romFolders.append(romFolder(romType.PRIMEHACK,    value))
                    case "3ds":          self.romFolders.append(romFolder(romType._3DS,         value))
                    case _:              Warning(f"invalid key '{key}' in 'romsFolder' of config file")
                # }
            # }
            if len(self.romFolders) == 0:
            # {
                raise ValueError("No valid rom folders found in config file")
            # }
        # }
        except KeyError:
        # {
            raise KeyError("Missing 'romPaths' in config file")
        # }
        except json.JSONDecodeError:    
        # {
            raise ValueError("invalid JSON found in config file")
        # }
    # }
# }
