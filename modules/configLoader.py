# ------------------------- #
# File:     configLoader.py
# Purpose:  open gui
# Python:   3.13.1
# Edited:   3/19/2026
# Author:   williambwb75
# ------------------------- #

from modules.directoryScanner   import directoryScanner
from modules.sharedTypes        import operatingSystem, romType
from modules.shortcutGenerator  import romFolder

import json

class configLoader:
# {
    def __init__(self, configFilePath):
    # {
        self.configFilePath = configFilePath
        self.__getOperatingSystem()
        self.__getRomPaths()
        self.__getOutputFolder()
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
                match folder:
                # {
                    case "nes":          self.romFolders.append(romFolder(romType.NES,          jsonFile["romsFolder"]+"\\nes"))
                    case "snes":         self.romFolders.append(romFolder(romType.SNES,         jsonFile["romsFolder"]+"\\snes"))
                    case "gba":          self.romFolders.append(romFolder(romType.GBA,          jsonFile["romsFolder"]+"\\gba"))
                    case "wii":          self.romFolders.append(romFolder(romType.WII,          jsonFile["romsFolder"]+"\\wii"))
                    case "primehack":    self.romFolders.append(romFolder(romType.PRIMEHACK,    jsonFile["romsFolder"]+"\\primehack"))
                    case "3ds":          self.romFolders.append(romFolder(romType._3DS,         jsonFile["romsFolder"]+"\\3ds"))
                    case _:              Warning(f"invalid value '{folder}' in 'romsFolder' of config file")
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

    def __getOutputFolder(self):
    # {
        try:
        # {
            with open(self.configFilePath) as file:
            # {
                jsonFile = json.load(file)
            # }
            self.outputFolder = jsonFile["outputFolder"]
        # }
        except KeyError:
        # {
            raise KeyError("Missing 'outputFolder' in config file")
        # }
        except json.JSONDecodeError:    
        # {
            raise ValueError("invalid JSON found in config file")
        # }
    # }
# }