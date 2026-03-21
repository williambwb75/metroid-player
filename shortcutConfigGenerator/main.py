from shortcutGeneratorJsonCreator import shortcutGeneratorJsonCreator
from dumpConfigFiles import dumpConfigFiles
from printStatus import *
import sys

def main(emulatorDataJson, validDirectoriesJson, inputDirectory, outputDirectory, shortcutTemplateDirectory, configFolderOutputDirectory):
    configFiles = shortcutGeneratorJsonCreator(emulatorDataJson, validDirectoriesJson, inputDirectory, outputDirectory, shortcutTemplateDirectory)
    if configFiles == False:
        printError("Failed to generate config files")
        quit()
    dumpConfigFiles(configFolderOutputDirectory, configFiles)
    printSuccess("Shortcut Config Generator executed successfully")

if __name__ == "__main__":
    if len(sys.argv) >= 6:
        main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    else:
        printError("Usage: python main.py emulatorDataJson, validDirectoriesJson, inputDirectory, outputDirectory, shortcutTemplateDirector")
        exit()