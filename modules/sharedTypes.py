# ------------------------- #
# File:     sharedTypes.py
# Purpose:  define shared types
# Python:   3.13.1
# Edited:   3/19/2026
# Author:   williambwb75
# ------------------------- #

from enum import Enum

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