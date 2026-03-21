import json
import os
import shutil

from printStatus import *

def emulatorDataLoader(configFilePath):
    configFile = openFile(configFilePath)
    if configFile == False:
        return False
    configJson = jsonFile(configFile)
    if configJson == False:
        return False
    if checkJsonStructure(configJson) == False:
        return False
    if checkJsonTypes(configJson) == False:
        return False
    if checkEmulatorData(configJson["emulatorData"]) == False:
        return False
    return configJson

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

def checkJsonStructure(configJson):
    if "emulatorData" not in configJson:
        printWarning("Missing required key: emulatorData")
        return False
    return True

def checkJsonTypes(configJson):
    if not isinstance(configJson["emulatorData"], dict):
        printWarning("emulatorData should be a dictionary.")
        return False
    return True

def checkEmulatorData(emulatorData):
    for emulatorName, emulatorConfig in emulatorData.items():
        if not isinstance(emulatorName, str):
            printWarning("Emulator names must be strings.")
            return False
        if not isinstance(emulatorConfig, dict):
            printWarning(f"{emulatorName} configuration should be a dictionary.")
            return False
        if checkRequiredKeys(emulatorName, emulatorConfig) == False:
            return False
        if checkExecutablePath(emulatorName, emulatorConfig["executablePath"]) == False:
            return False
        if checkArguments(emulatorName, emulatorConfig["arguments"]) == False:
            return False
    return True

def checkRequiredKeys(emulatorName, emulatorConfig):
    if "executablePath" not in emulatorConfig:
        printWarning(f"Missing executablePath in {emulatorName}.")
        return False
    if "arguments" not in emulatorConfig:
        printWarning(f"Missing arguments in {emulatorName}.")
        return False
    return True

def checkExecutablePath(emulatorName, executablePath):
    if not isinstance(executablePath, str):
        printWarning(f"executablePath in {emulatorName} should be a string.")
        return False
    if shutil.which(executablePath) is None and not os.path.isfile(executablePath):
        printWarning(f"Executable not found for {emulatorName}: {executablePath}")
        return False
    return True

def checkArguments(emulatorName, arguments):
    if not isinstance(arguments, list):
        printWarning(f"arguments in {emulatorName} should be a list.")
        return False
    if not all(isinstance(arg, str) for arg in arguments):
        printWarning(f"All arguments in {emulatorName} should be strings.")
        return False
    if not any("{filePath}" in arg for arg in arguments):
        printWarning(f"{{filePath}} placeholder not found in arguments for {emulatorName}.")
        return False
    return True