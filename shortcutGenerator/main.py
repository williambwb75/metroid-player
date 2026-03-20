from configLoader import configLoader
from commandGenerator import commandGenerator
from shortcutGenerator import shortcutGenerator
from printStatus import *

def main(configFilePath):
    config = configLoader(configFilePath)
    if config == False:
        printError("Config loading failed. Exiting.")
        exit()
    printInfo("Config loaded successfully.")
    commands = commandGenerator(config)
    if commands == False:
        printError("Command generation failed. Exiting.")
        exit()
    printInfo("Commands generated successfully.")
    if shortcutGenerator(config["inputDirectory"], config["outputDirectory"], config["targetFileExtension"], config["shortcutTemplate"], commands) == False:
        printError("Shortcut generation failed. Exiting.")
        exit()
    printInfo("Commands generated successfully.")
    printSuccess("Application executed successfully.")