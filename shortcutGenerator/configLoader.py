import json
import shutil
import os

from printStatus import *

def configLoader(configFilePath):
    configFile = openFile(configFilePath)
    if configFile == False: 
        return False
    configJson = jsonFile(configFile)
    if configJson == False: 
        return False
    if checkJsonTypes(configJson) == False: 
        return False
    if checkDirectory(configJson["inputDirectory"]) == False: 
        return False
    if checkDirectory(configJson["outputDirectory"]) == False: 
        return False
    if checkDirectoryContainsFiles(configJson["inputDirectory"], configJson["targetFileExtension"]) == False:
        return False
    # if checkTargetApplication(configJson["applicationPath"]) == False:
    #     return False
    if checkTargetApplicationArguments(configJson["applicationArguments"]) == False:
        return False
    if checkShortcutTemplateExists(configJson["shortcutTemplate"]) == False:
        return False
    if checkShortcutTemplateContents(openFile(configJson["shortcutTemplate"])) == False:
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
    
def checkDirectory(directoryPath):
    if not os.path.exists(directoryPath):
        printWarning(f"Directory does not exist: {directoryPath}")
        return False
    return True

def checkDirectoryContainsFiles(directoryPath, fileExtension):
    files = [f for f in os.listdir(directoryPath) if f.endswith(fileExtension)]
    if not files:
        printWarning(f"No files with extension {fileExtension} found in directory: {directoryPath}")
        return False
    return True

def checkTargetApplication(applicationPath):
    if shutil.which(applicationPath) is None:
        printWarning(f"Target application not found: {applicationPath}")
        return False
    return True

def checkTargetApplicationArguments(applicationArguments):
    if not any("{filePath}" in arg for arg in applicationArguments):   
        printWarning("{filePath} placeholder not found in applicationArguments.")
        return False
    return True

def checkShortcutTemplateExists(templatePath):
    if not os.path.isfile(templatePath):
        printWarning(f"Shortcut template file not found: {templatePath}")
        return False
    return True

def checkShortcutTemplateContents(template):
    if "{name}" not in template:
        printWarning("{name} placeholder not found in shortcutNameTemplate.")
        return False
    if "{command}" not in template:
        printWarning("{command} placeholder not found in shortcutNameTemplate.")
        return False
    if "{icon}" not in template:
        printWarning("{icon} placeholder not found in shortcutNameTemplate.")
        return False
    return True

def checkJsonTypes(configJson):
    if not isinstance(configJson["inputDirectory"], str):
        printWarning("inputDirectory should be a string.")
        return False
    if not isinstance(configJson["outputDirectory"], str):
        printWarning("outputDirectory should be a string.")
        return False
    if not isinstance(configJson["targetFileExtension"], str):
        printWarning("targetFileExtension should be a string.")
        return False
    if not isinstance(configJson["applicationPath"], str):
        printWarning("applicationPath should be a string.")
        return False
    if not isinstance(configJson["applicationArguments"], list):
        printWarning("applicationArguments should be a list.")
        return False
    if not all(isinstance(arg, str) for arg in configJson["applicationArguments"]):
        printWarning("all items in applicationArguments should be strings.")
        return False
    if not isinstance(configJson["shortcutTemplate"], str):
        printWarning("shortcutTemplate should be a string.")
        return False
    return True