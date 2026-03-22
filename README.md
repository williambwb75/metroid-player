# Metroid Player – Shortcut Generator

Metroid Player is a small GUI tool that scans your ROM folder and automatically generates launchable shortcuts for each game. 

I made this tool as I was playing through every metroid game and got tired of opening emulators.

It uses a template file and a JSON‑defined folder structure (romFolderStructure+OperatingSystem) to decide how shortcuts should be built for each system.

---

## Usage

- If on windows rum 'start.bat' to get you going
- If on linux run 'start.sh' to get you going
- Developed with python 3.11.6 installed and working, but i expect any python 3.x version will work fine

- When running a GUI will open asking for 4 feilds:
- - input roms folder
- - output shortcuts folder
- - shortcut template (auto loaded example)
- - rom folder structure (auto loaded example)

- Press generate button and after a few seconds will receive a popup to confirm shortcuts created
- If it didnt work check the romFileStructure to see arguments, file-extensions etc and customise as needed

---

## What It Does

- Detects ROM subfolders (defined in romFolderStructure json)
- Reads the correct file extension + emulator command from a JSON structure file
- Generates shortcuts (.desktop on Linux, .bat on Windows) for every ROM found
- Outputs shortcuts into a mirrored folder structure
- Shortcut templates can have arguments {command} {name} {filePath} for each one. Only {command} & {filePath} is needed
- Note: I do plan to support {icon} in the future if this project continues, currently does nothing

---

## How It Works

You select:
 - Input directory (your ROM folders)
 - Output directory (where shortcuts go)
 - Shortcut template file
 - ROM folder structure JSON

The Tool:
 - Loads the JSON structure
 - Scans each defined subfolder
 - Creates a temporary config
 - Calls the shortcut generator
 - Produces shortcuts using your template

---

My roms/emulator is not in romFileStructure

- Thats ok, just add to the json of your os and create a pr, i would be happy to add more to these json files
- If wanting a different emulator I might be more hesitant to accept since what is in the json is working fine