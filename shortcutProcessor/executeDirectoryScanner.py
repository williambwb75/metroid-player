import os
import json

from printStatus import *

def executeDirectoryScanner(romFileStructurePath, inputFolderName, outputFileName):
    os.chdir("..")
    os.chdir("directoryScanner")
    os.system(f"py main.py {romFileStructurePath} {inputFolderName} {outputFileName}")
    if not os.path.isfile(outputFileName):
        printWarning(f"Directory Scanner output file not found: {outputFileName}")
        return False
    with open(outputFileName, 'r') as f:
        lines = f.read().splitlines()
    lines = json.loads(''.join(lines))  
    os.remove(outputFileName)
    os.chdir("..")
    os.chdir("shortcutProcessor")
    return lines