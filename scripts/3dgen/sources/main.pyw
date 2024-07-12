import tkinter as tk
from tkinter import filedialog
import asset_werkzeug

class App:
    def __init__(self, master):
        self.master = master
        master.title("Asset Generator")

        self.tag_label = tk.Label(master, text="TAG")
        self.tag_label.pack()

        self.tag_entry = tk.Entry(master)
        self.tag_entry.pack()

        self.path_label = tk.Label(master, text="Folder")
        self.path_label.pack()

        self.select_button = tk.Button(master, text="Select folder", command=self.select_folder)
        self.select_button.pack()

        self.generate_button = tk.Button(master, text="Generate", command=self.generate_assets)
        self.generate_button.pack()

        self.selected_path = None

    def select_folder(self):
        self.selected_path = filedialog.askdirectory()

    def generate_assets(self):
        tag = self.tag_entry.get()
        if self.selected_path:
            asset_werkzeug.AssetWerkzeug.create_asset_file(tag, self.selected_path)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
