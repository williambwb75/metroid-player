import os

from printStatus import *

def commandGenerator(configJson):
    files = scanDirectoryForFiles(configJson["inputDirectory"], configJson["targetFileExtension"])
    if files == False:
        return False
    commands = createCommandForFiles(files, configJson["inputDirectory"], configJson["applicationPath"], configJson["applicationArguments"])
    if commands == False:
        return False
    return commands

def scanDirectoryForFiles(directoryPath, fileExtension):
    files = [f for f in os.listdir(directoryPath) if f.endswith(fileExtension)]
    if not files:
        printWarning(f"No files with extension {fileExtension} found in directory: {directoryPath}")
        return False
    return files

def createCommand(applicationPath, applicationArguments, filePath):
    if not applicationPath or not os.path.exists(applicationPath):
        printWarning(f"Application path does not exist: {applicationPath}")
        return False
    if not filePath or not os.path.exists(filePath):
        printWarning(f"File path does not exist: {filePath}")
        return False
    if not applicationArguments:
        printWarning("Application arguments are missing.")
        return False
    hasFilepathPlaceholder = any("{filePath}".lower() in arg.lower() for arg in applicationArguments)
    if not hasFilepathPlaceholder:
        printWarning("{filePath} placeholder not found in applicationArguments.")
        return False
    command = [applicationPath]
    for arg in applicationArguments:
        command.append(arg.replace("{filePath}", filePath))
    return ' '.join(f'"{arg}"' for arg in command)

def createCommandForFiles(files, inputDirectory, applicationPath, applicationArguments):
    commands = []
    for file in files:
        filePath = os.path.join(inputDirectory, file)
        command = createCommand(applicationPath, applicationArguments, filePath)
        if command is False:
            printWarning(f"Failed to create command for file: {file}")
            return False
        commands.append(command)
    return commands if commands else False