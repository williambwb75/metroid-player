import json
import os

from printStatus import *

def romFileStructureLoader(romFileStructurePath):
    romFileStructure = openFile(romFileStructurePath)
    if romFileStructure == False:
        return False
    romFileStructureJson = jsonFile(romFileStructure)
    if romFileStructureJson == False:
        return False
    if checkJsonStructure(romFileStructureJson) == False:
        return False
    if checkJsonTypes(romFileStructureJson) == False:
        return False
    if checkDirectory(romFileStructureJson["romFilePath"]) == False:
        return False
    if checkRomFileStructure(romFileStructureJson["romFileStructure"]) == False:
        return False
    romFileStructureJson["romFileStructure"] = checkRomDirectoriesContainFiles(romFileStructureJson["romFilePath"], romFileStructureJson["romFileStructure"])
    return romFileStructureJson

def openFile(filePath):
    try:
        with open(filePath, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        printWarning(f"File not found: {filePath}")
        return False
    except Exception as error:
        printWarning(f"Error reading file {filePath}: {error}")
        return False

def jsonFile(content):
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        printWarning("Invalid JSON found in config file.")
        return False

def checkJsonStructure(romFileStructureJson):
    requiredKeys = ["romFilePath", "romFileStructure"]
    for key in requiredKeys:
        if key not in romFileStructureJson:
            printWarning(f"Missing required key: {key}")
            return False
    return True

def checkJsonTypes(romFileStructureJson):
    if not isinstance(romFileStructureJson["romFilePath"], str):
        printWarning("romFilePath should be a string.")
        return False
    if not isinstance(romFileStructureJson["romFileStructure"], dict):
        printWarning("romFileStructure should be a dictionary.")
        return False
    return True

def checkDirectory(directoryPath):
    if not os.path.exists(directoryPath):
        printWarning(f"Directory does not exist: {directoryPath}")
        return False
    return True

def checkRomFileStructure(structure):
    for systemName, systemConfig in structure.items():
        if not isinstance(systemName, str):
            printWarning("System names in romFileStructure must be strings.")
            return False
        if not isinstance(systemConfig, dict):
            printWarning(f"{systemName} configuration should be a dictionary.")
            return False
        if "fileExtension" not in systemConfig:
            printWarning(f"Missing fileExtension in {systemName}.")
            return False
        if "emulatorType" not in systemConfig:
            printWarning(f"Missing emulatorType in {systemName}.")
            return False
        if not isinstance(systemConfig["fileExtension"], str):
            printWarning(f"fileExtension in {systemName} should be a string.")
            return False
        if not systemConfig["fileExtension"].startswith("."):
            printWarning(f"fileExtension in {systemName} should start with a '.'.")
            return False
        if not isinstance(systemConfig["emulatorType"], str):
            printWarning(f"emulatorType in {systemName} should be a string.")
            return False
    return True

def checkRomDirectoriesContainFiles(basePath, structure):
    for systemName, systemConfig in list(structure.items()):
        systemPath = os.path.join(basePath, systemName)
        if not os.path.exists(systemPath):
            printWarning(f"Directory for system '{systemName}' does not exist: {systemPath}")
            structure.pop(systemName, None)
            continue

        files = [f for f in os.listdir(systemPath) if f.endswith(systemConfig["fileExtension"])]
        if not files:
            printWarning(
                f"No files with extension {systemConfig['fileExtension']} found in {systemPath}"
            )
            return False
    return structure