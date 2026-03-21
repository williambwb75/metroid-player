import json
import os

def dumpConfigFiles(configFolderOutputDirectory, configFiles):
    for index, configFile in enumerate(configFiles):
        with open(configFile, 'r') as f:
            data = json.load(f)
        output_path = os.path.join(configFolderOutputDirectory, f'config_{index}.json')
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=2)