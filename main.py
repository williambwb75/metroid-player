import tkinter as tk
from tkinter import filedialog, messagebox
import json
import platform
import os

def add_row(root, label_text, row, browse_type=None, browse_directory_fn=None, browse_file_fn=None):
    label = tk.Label(root, text=label_text)
    label.grid(row=row, column=0, sticky="w", padx=10, pady=5)

    entry = tk.Entry(root, width=60)
    entry.grid(row=row, column=1, padx=10)

    if browse_type == "folder":
        btn = tk.Button(root, text="Browse", command=lambda: browse_directory_fn(entry))
        btn.grid(row=row, column=2, padx=5)

    elif browse_type == "file":
        btn = tk.Button(root, text="Browse", command=lambda: browse_file_fn(entry))
        btn.grid(row=row, column=2, padx=5)

    return entry


def browse_directory(entry_widget):
    path = filedialog.askdirectory()
    if path:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, path)


def browse_file(entry_widget):
    path = filedialog.askopenfilename()
    if path:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, path)


def generate_shortcuts(entries):
    input_root = entries["input"].get()
    output_root = entries["output"].get()
    template_local = entries["template"].get()

    if not input_root or not output_root:
        messagebox.showerror("Error", "Input and Output directories must be selected.")
        return

    if not os.path.isdir(input_root):
        messagebox.showerror("Error", "Input directory does not exist.")
        return

    os.makedirs(output_root, exist_ok=True)

    process_subfolders(input_root, output_root, template_local)

    messagebox.showinfo("Done", "Shortcuts generated for all detected ROM folders.")


def load_existing_config(entries, config):
    entries["input"].insert(0, config.get("inputDirectory", ""))
    entries["output"].insert(0, config.get("outputDirectory", ""))
    entries["template"].insert(0, config.get("shortcutTemplate", ""))


def main():
    root = tk.Tk()
    root.title("Shortcut Generator")

    root.update_idletasks()
    root.minsize(root.winfo_width(), root.winfo_height())

    entries = {}
    entries["input"] = add_row(root, "Input Directory:", 0, "folder", browse_directory_fn=browse_directory)
    entries["output"] = add_row(root, "Output Directory:", 1, "folder", browse_directory_fn=browse_directory)
    entries["template"] = add_row(root, "Shortcut Template File:", 2, "file", browse_file_fn=browse_file)

    save_button = tk.Button(root, text="Generate", command=lambda: generate_shortcuts(entries), width=20)
    save_button.grid(row=3, column=1, pady=20)

    existing_config = {
        "inputDirectory": "",
        "outputDirectory": "",
        "shortcutTemplate": ""
    }
    if platform.system() == "Linux":
        existing_config["shortcutTemplate"] = "template.desktop"
    elif platform.system() == "Windows":
        existing_config["shortcutTemplate"] = "template.bat"

    load_existing_config(entries, existing_config)
    root.mainloop()

def load_rom_structure():
    with open("romFolderStructure"+platform.system()+".json", "r") as f:
        return json.load(f)["subFolders"]

def process_subfolders(input_root, output_root, shortcut_directory):
    rom_structure = load_rom_structure()

    for folder_name, settings in rom_structure.items():
        input_sub = os.path.join(input_root, folder_name)
        output_sub = os.path.join(output_root, folder_name)

        if os.path.isdir(input_sub):
            print(f"Found ROM folder: {folder_name}")

            os.makedirs(output_sub, exist_ok=True)

            config_data = {
                "inputDirectory": input_sub,
                "outputDirectory": output_sub,
                "targetFileExtension": settings["fileExtension"],
                "applicationPath": settings["application"],
                "applicationArguments": settings["arguments"],
                "shortcutTemplate": f"../{shortcut_directory}"
            }

            with open("config.json", "w") as file:
                json.dump(config_data, file, indent=4)

            os.chdir("shortcutGenerator")
            if platform.system() == "Linux":
                os.system("python main.py ../config.json")
            elif platform.system() == "Windows":
                os.system("py main.py ../config.json")
            os.chdir("..")

            os.remove("config.json")

if __name__ == "__main__":
    main()
