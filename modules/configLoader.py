# ------------------------- #
# File:     configLoader.py
# Purpose:  open gui
# Python:   3.13.1
# Edited:   3/19/2026
# Author:   williambwb75
# ------------------------- #

from enum import Enum
import json

class operatingSystem(Enum):
# {
    LINUX   = 0
    WINDOWS = 1
# }

class configLoader:
# {
    def __init__(self, configFilePath):
    # {
        self.configFilePath = configFilePath
        self.__getOperatingSystem()
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
                case _: raise TypeError("invalid 'operatingSystem' found in config")
            # }
        # }
        except FileNotFoundError:
        # {
            print("Config file not found:", self.configFilePath)
        # }
        except KeyError:
        # {
            raise KeyError("Missing 'operatingSystem' in config file")
        # }
        except json.JSONDecodeError:
        # {
            raise ValueError("Config file contains invalid JSON")
        # }
    # }
# }
