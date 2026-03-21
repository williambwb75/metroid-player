import tkinter as tk
from tkinter import filedialog, messagebox
import json
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
    config_data = {
        "inputDirectory": entries["input"].get(),
        "outputDirectory": entries["output"].get(),
        "targetFileExtension": entries["ext"].get(),
        "applicationPath": entries["app"].get(),
        "applicationArguments": entries["args"].get().split(";"),
        "shortcutTemplate": entries["template"].get()
    }

    if not all(config_data.values()):
        messagebox.showerror("Error", "All fields must be filled.")
        return

    with open("config.json", "w") as file:
        config_data["shortcutTemplate"] = "../"+config_data["shortcutTemplate"]
        json.dump(config_data, file, indent=4)

    os.chdir("shortcutGenerator")
    os.system("python main.py ../config.json")
    os.chdir("..")


def load_existing_config(entries, config):
    entries["input"].insert(0, config.get("inputDirectory", ""))
    entries["output"].insert(0, config.get("outputDirectory", ""))
    entries["ext"].insert(0, config.get("targetFileExtension", ""))
    entries["app"].insert(0, config.get("applicationPath", ""))
    entries["args"].insert(0, ";".join(config.get("applicationArguments", [])))
    entries["template"].insert(0, config.get("shortcutTemplate", ""))


def main():
    root = tk.Tk()
    root.title("Shortcut Generator")

    root.update_idletasks()
    root.minsize(root.winfo_width(), root.winfo_height())

    entries = {}
    entries["input"] = add_row(root, "Input Directory:", 0, "folder", browse_directory_fn=browse_directory)
    entries["output"] = add_row(root, "Output Directory:", 1, "folder", browse_directory_fn=browse_directory)
    entries["ext"] = add_row(root, "Target File Extension (.txt):", 2)
    entries["app"] = add_row(root, "Application Path:", 3, "file", browse_file_fn=browse_file)
    entries["args"] = add_row(root, "Application Arguments (semicolon-separated):", 4)
    entries["template"] = add_row(root, "Shortcut Template File:", 5, "file", browse_file_fn=browse_file)

    save_button = tk.Button(root, text="Generate", command=lambda: generate_shortcuts(entries), width=20)
    save_button.grid(row=6, column=1, pady=20)

    existing_config = {
        "inputDirectory": "",
        "outputDirectory": "",
        "targetFileExtension": "",
        "applicationPath": "",
        "applicationArguments": ["{filePath}"],
        "shortcutTemplate": "template.desktop"
    }

    load_existing_config(entries, existing_config)
    root.mainloop()

if __name__ == "__main__":
    main()
