# Input

# validDirectoriesJson
# {'romFilePath': 'C:\\Users\\William\\Desktop\\metroid-player\\roms', 'romFileStructure': {'nes': {'fileExtension': '.nes', 'emulatorType': 'nes'}, 'snes': {'fileExtension': '.sfc', 'emulatorType': 'snes'}}}

# emulatorData.json 
# {
#     "emulatorData":
#     {
#         "nes":
#         {
#             "executablePath": "C:\\Users\\William\\Downloads\\iNES61-Windows-bin\\iNES.exe",
#             "arguments": ["{filePath}"]
#         },
#         "snes":
#         {
#             "executablePath": "C:\\Users\\William\\Downloads\\snes9x-1.63-win32-x64\\snes9x-x64.exe",
#             "arguments": ["{filePath}"]
#         },
#         "gba":
#         {
#             "executablePath": "C:\\Users\\William\\Downloads\\mGBA-0.10.5-win32\\mGBA-0.10.5-win32\\mGBA.exe",
#             "arguments": ["{filePath}"]
#         }
#     }
# }

# Example output:

# Will need to create a jsonConfig for each rom
# {
#     "inputDirectory": "C:\\Users\\William\\Desktop\\metroid-player\\input",
#     "outputDirectory": "C:\\Users\\William\\Desktop\\metroid-player\\output",
#     "targetFileExtension": ".sfc",
#     "applicationPath": "C:\\Users\\William\\Downloads\\snes9x-1.62.3-win32-x64\\snes9x-x64.exe",
#     "applicationArguments": 
#     [
#         "--batch",
#         "--exec={filePath}"
#     ],
#     "shortcutTemplate": "template.desktop"
# }

import os
import json

from printStatus import *

def shortcutGeneratorJsonCreator(emulatorData, validDirectoriesJson, inputDirectory, outputDirectory, templateDirectory):
    with open(validDirectoriesJson, 'r') as f:
        rom_structure = json.loads(validDirectoriesJson)
    rom_structure = rom_structure["romFileStructure"]
    os.makedirs(outputDirectory, exist_ok=True)
    generated_json = []
    for system_name, system_info in rom_structure.items():
        system_dir = os.path.join(inputDirectory, system_name)

        if not os.path.isdir(system_dir):
            printInfo(f"Skipping missing directory: {system_dir}", "warn")
            continue

        expected_ext = system_info["fileExtension"]
        emulator_type = system_info["emulatorType"]

        if emulator_type not in emulatorData["emulatorData"]:
            printInfo(f"No emulator config for type '{emulator_type}'", "error")
            continue

        emulator_cfg = emulatorData["emulatorData"][emulator_type]

        for file in os.listdir(system_dir):
            if not file.lower().endswith(expected_ext):
                continue

            json_config = {
                "inputDirectory": inputDirectory+"\\"+system_name,
                "outputDirectory": outputDirectory+"\\"+system_name,
                "targetFileExtension": expected_ext,
                "applicationPath": emulator_cfg["executablePath"],
                "applicationArguments": emulator_cfg["arguments"],
                "shortcutTemplate": templateDirectory
            }

        generated_json.append(json_config)

    return generated_json
