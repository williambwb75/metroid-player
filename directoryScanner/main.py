import sys
from printStatus import *

from romFileStructureLoader import romFileStructureLoader
from directoryDumper import directoryDumper

def main(romFileStructure, outputFileName="output.txt"):
    romFileStructureConfig = romFileStructureLoader(romFileStructure)
    if romFileStructureConfig == False:
        printError("ROM file structure loading failed. Exiting.")
        exit() 
    printInfo("ROM file structure loaded successfully.")
    directoryDumper(romFileStructureConfig, outputFileName)
    printInfo(f"Directory structure dumped to {outputFileName}.")
    printSuccess("Directory Scanner executed successfully.")

if __name__ == "__main__":
    if len(sys.argv) <= 2:
        printError("Usage: python main.py <romFileStructure> <outputFileName>")
        exit()
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main(sys.argv[1], sys.argv[2])