import os
from printStatus import *

def shortcutGenerator(inputDirectory, outputDirectory, targetFileExtension, shortcutTemplate, commands):
    if checkOutputDirectory(outputDirectory) == False:
        return False
    if checkCommands(commands) == False:
        return False
    if checkOutputDirectoryWritable(outputDirectory) == False:
        return False
    if checkOutputDirectoryExists(outputDirectory) == False:
        return False
    template = openTemplate(shortcutTemplate)
    if template == False:
        return False
    filenames = fetchFilenames(inputDirectory, targetFileExtension)
    if filenames == False:
        return False
    if len(commands) != len(filenames):
        printWarning("Number of commands does not match number of files.")
        return False
    printWarning("Erasing contents of output directory.")
    for filename in os.listdir(outputDirectory):
        filePath = os.path.join(outputDirectory, filename)
        if os.path.isfile(filePath):
            os.remove(filePath)
    for i, command in enumerate(commands):
        filename = filenames[i]
        icon = '""'
        generateShortcut(outputDirectory, shortcutTemplate, command, filename, icon, targetFileExtension)
    return True

def openTemplate(templatePath):
    if not os.path.isfile(templatePath):
        printWarning(f"Shortcut template file not found: {templatePath}")
        return False
    with open(templatePath, "r") as templateFile:
        template = templateFile.read()
    if "{name}" not in template:
        printWarning("{name} placeholder not found in shortcutNameTemplate.")
        return False
    if "{command}" not in template:
        printWarning("{command} placeholder not found in shortcutNameTemplate.")
        return False
    if "{icon}" not in template:
        printWarning("{icon} placeholder not found in shortcutNameTemplate.")
        return False
    return template

def checkOutputDirectory(outputDirectory):
    if not os.path.exists(outputDirectory):
        printWarning(f"Output directory does not exist: {outputDirectory}")
        return False
    if not os.path.isdir(outputDirectory):
        printWarning(f"Output path is not a directory: {outputDirectory}")
        return False
    
def checkCommands(commands):
    if not isinstance(commands, list):
        printWarning("Commands should be a list.")
        return False
    for command in commands:
        if not isinstance(command, str):
            printWarning("Each command should be a string.")
            return False
    return True

def checkOutputDirectoryWritable(outputDirectory):
    if not os.access(outputDirectory, os.W_OK):
        printWarning(f"Output directory is not writable: {outputDirectory}")
        return False
    return True

def checkOutputDirectoryExists(outputDirectory):
    if not os.path.exists(outputDirectory):
        printWarning(f"Output directory does not exist: {outputDirectory}")
        return False
    return True

def fetchFilenames(inputDirectory, targetFileExtension):
    files = [f for f in os.listdir(inputDirectory) if f.endswith(targetFileExtension)]
    if not files:
        printWarning(f"No files with extension {targetFileExtension} found in directory: {inputDirectory}")
        return False
    return files

def generateShortcut(outputDirectory, shortcutTemplate, command, filename, icon, targetFileExtension):
    with open(shortcutTemplate, "r") as templateFile:
        template = templateFile.read()
    name = os.path.splitext(filename)[0]
    name = name.replace(f".{targetFileExtension}", "")
    template = template.replace("{name}", name)
    template = template.replace("{command}", command)
    template = template.replace("{icon}", icon)
    templateFileExtension = shortcutTemplate.split(".")[-1]
    shortcutPath = os.path.join(outputDirectory, f"{name}.{templateFileExtension}")
    with open(shortcutPath, "w") as shortcutFile:
        shortcutFile.write(template)