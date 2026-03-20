from configLoader import configLoader
from commandGenerator import commandGenerator
from shortcutGenerator import shortcutGenerator
from printStatus import *

if __name__ == "__main__":
    config = configLoader("generationData\\config.json")
    if config == False:
        printError("Config loading failed. Exiting.")
        exit()
    printInfo("Config loaded successfully.")
    commands = commandGenerator(config)
    if commands == False:
        printError("Command generation failed. Exiting.")
        exit()
    if shortcutGenerator(config["inputDirectory"], config["outputDirectory"], config["applicationPath"], config["targetFileExtension"], config["shortcutTemplate"], commands) == False:
        printError("Shortcut generation failed. Exiting.")
        exit()
    printInfo("Commands generated successfully.")
    printSuccess("Application executed successfully.")