import os

# os.chdir("shortcutGenerator")
# os.system("py main.py")

# os.chdir("directoryScanner")
# os.system("py main.py C:\\Users\\William\\Desktop\\metroid-player\\directoryScanner\\generationData\\romFileStructure.json")

os.chdir("shortcutProcessor")
os.system("py main.py applicationData.json emulatorData.json C:\\Users\\William\\Desktop\\metroid-player\\roms C:\\Users\\William\\Desktop\\metroid-player\\output")