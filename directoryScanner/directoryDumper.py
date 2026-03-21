import json
import os

def directoryDumper(romFileStructureConfig, outputFileName):
    with open(outputFileName, 'w') as f:
        json.dump(romFileStructureConfig, f, indent=2)