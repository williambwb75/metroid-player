import os
import json
from printStatus import *

def executeShortcutGenerator(shortcutGeneratorConfigFiles):
    os.chdir("..")
    os.chdir("shortcutGenerator")

    configFileName = "config.json"
    for configFile in shortcutGeneratorConfigFiles:
        with open(configFileName, "w") as f:
            json.dump(configFile, f)
        os.makedirs(configFile["outputDirectory"], exist_ok=True)
        os.system(f"py main.py {configFileName}")

    os.remove(configFileName)
    os.chdir("..")
    os.chdir("shortcutProcessor")
    
    return True