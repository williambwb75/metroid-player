import json
import os

from printStatus import *

def applicationDataLoader(applicationDataFilePath):
    applicationDataFile = openFile(applicationDataFilePath)
    if applicationDataFile == False:
        return False
    applicationDataJson = jsonFile(applicationDataFile)
    if applicationDataJson == False:
        return False
    if checkJsonStructure(applicationDataJson) == False:
        return False
    if checkJsonTypes(applicationDataJson) == False:
        return False
    if checkDirectoryScanner(applicationDataJson["directoryScanner"]) == False:
        return False
    if checkRomFileStructurePath(applicationDataJson["directoryScanner"]["romFileStructure"]) == False:
        return False
    return applicationDataJson

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
        printWarning("Invalid JSON found in applicationData file.")
        return False

def checkJsonStructure(applicationDataJson):
    if "directoryScanner" not in applicationDataJson:
        printWarning("Missing required key: directoryScanner")
        return False
    return True

def checkJsonTypes(applicationDataJson):
    if not isinstance(applicationDataJson["directoryScanner"], dict):
        printWarning("directoryScanner should be a dictionary.")
        return False
    return True

def checkDirectoryScanner(directoryScanner):
    if "romFileStructure" not in directoryScanner:
        printWarning("Missing required key: romFileStructure in directoryScanner")
        return False
    return True

def checkRomFileStructurePath(filePath):
    if not isinstance(filePath, str):
        printWarning("romFileStructure should be a string path.")
        return False
    os.chdir("..")
    os.chdir("directoryScanner")
    if not os.path.isfile(filePath):
        printWarning(f"romFileStructure file not found: {filePath}")
        return False
    content = openFile(filePath)
    if content == False:
        return False
    parsed = jsonFile(content)
    if parsed == False:
        printWarning("romFileStructure file contains invalid JSON.")
        return False
    os.chdir("..")
    os.chdir("shortcutProcessor")
    return True