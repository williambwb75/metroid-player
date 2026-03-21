import sys
from printStatus import *
from applicationDataLoader import applicationDataLoader
from emulatorDataLoader import emulatorDataLoader
from executeDirectoryScanner import executeDirectoryScanner
from shortcutGeneratorJsonCreator import shortcutGeneratorJsonCreator
from executeShortcutGenerator import executeShortcutGenerator

def main(applicationData, emulatorData, romFolderPath, outputFolder):
    applicationData = applicationDataLoader(applicationData)
    if applicationData == False:
        printError("Failed to load application data.")
        exit()
    printInfo("Application data loaded successfully.")
    emulatorData = emulatorDataLoader(emulatorData)
    if emulatorData == False:
        printError("Failed to load emulator data.")
        exit()
    validDirectoriesJson = executeDirectoryScanner(applicationData["directoryScanner"]["romFileStructure"], applicationData["directoryScanner"]["outputFileName"])
    printInfo("Directory Scanner executed successfully.")
    shortcutGeneratorConfigFiles = shortcutGeneratorJsonCreator(emulatorData, validDirectoriesJson, outputFolder)
    if shortcutGeneratorConfigFiles == False:
        print("Failed to generate config files.")
        exit()
    printInfo("Shortcut Generator Json Creator executed successfully.")
    if not executeShortcutGenerator(shortcutGeneratorConfigFiles):
        print("Failed to execute shortcut generator.")
        exit()
    printInfo("Shortcut Generator executed successfully.")
    printSuccess("Shortcut Processor executed successfully.")

if __name__ == "__main__":
    if len(sys.argv) <= 4:
        printError("Usage: python main.py <applicationData> <emulatorData> <romFilePath> <outputFolder>")
        exit()
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])