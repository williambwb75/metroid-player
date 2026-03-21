import sys
from printStatus import *

from romFileStructureLoader import romFileStructureLoader
from directoryDumper import directoryDumper

def main(romFileStructure, inputPath, outputFileName):
    romFileStructureConfig = romFileStructureLoader(romFileStructure, inputPath)
    if romFileStructureConfig == False:
        printError("ROM file structure loading failed. Exiting.")
        exit() 
    printInfo("ROM file structure loaded successfully.")
    directoryDumper(romFileStructureConfig, outputFileName)
    printInfo(f"Directory structure dumped to {outputFileName}.")
    printSuccess("Directory Scanner executed successfully.")

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        printError("Usage: python main.py <romFileStructure> <inputPath> <outputFileName>")
        exit()