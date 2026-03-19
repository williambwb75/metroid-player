# ------------------------- #
# File:     main.py
# Purpose:  open gui
# Python:   3.13.1
# Edited:   3/19/2026
# Author:   williambwb75
# ------------------------- #

from modules.configLoader import configLoader

def main():
# {
    config = configLoader("config\\config.json")
    return 0
# }

if __name__ == "__main__":
# {
    main()
# }