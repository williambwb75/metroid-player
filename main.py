import os
import tkinter as tk
from tkinter import filedialog
import json

# def main():
#     applicationData = "applicationData.json"
#     emulatorData = "emulatorData.json"
#     templateDirectory = "../template.desktop"
#     root = tk.Tk()
#     root.withdraw()
#     tk.messagebox.showinfo("ROM Folder", "Please select the folder containing your ROM files")
#     romFolderPath = filedialog.askdirectory(title="Select ROM Folder")
#     tk.messagebox.showinfo("Output Folder", "Please select the folder where output files will be saved")
#     outputFolderPath = filedialog.askdirectory(title="Select Output Folder")
#     root.destroy()
#     os.chdir("shortcutProcessor")
#     os.system(f"py main.py {applicationData} {emulatorData} {romFolderPath} {outputFolderPath} {templateDirectory}")

def main():
    inputRomFolderPath =    "C:\\Users\\William\\Desktop\\roms"
    outputShortcutPath =    "C:\\Users\\William\\Desktop\\output"
    romFileStructure =      "..\\romFileStructure.json"
    directoryScannerDump =  "output.json"
    emulatorData =          "..\\emulatorData.json"
    shortcutTemplatePath =  "..\\template.desktop"
    romFileStructureName =  "romFileStructureOutput.json"
    currentPath =           os.path.dirname(os.path.abspath(__file__))+"configOutput\\"

    os.chdir("directoryScanner")
    print("Executing Directory Scanner")
    os.system(f"py main.py {romFileStructure} {inputRomFolderPath} {directoryScannerDump}")
    with open(directoryScannerDump, 'r') as f:
        romFileStructureJson = json.load(f)
    os.chdir("..")
    with open(romFileStructureName, 'w') as f:
        json.dump(romFileStructureJson, f)

    os.chdir("shortcutConfigGenerator")
    print("Executing Shortcut Generator")
    os.system(f"py main.py {emulatorData} ..\\{romFileStructureName} {inputRomFolderPath} {outputShortcutPath} {shortcutTemplatePath} {currentPath}")

if __name__ == "__main__":
    main()