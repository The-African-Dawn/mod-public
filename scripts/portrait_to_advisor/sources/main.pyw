import tkinter as tk
from tkinter import filedialog
import os
import portrait_werkzeug

class App():
    def process_and_save(file_path):
        """
        A function that processes and saves images, generating two image files based on the input file path.
        
        Args:
            file_path (str): The path to the input image file.
        
        Returns:
            None
        """
        base_name = os.path.basename(file_path)
        name, ext = os.path.splitext(base_name)
        output_file = os.path.join(os.path.dirname(file_path), f'{name}_output{ext}')
        combined_file = os.path.join(os.path.dirname(file_path), f'{name}_advisor{ext}')
        new_size = (65, 67)
        position = (6, 6)
        portrait_werkzeug.PortraitWerkzeug.process_and_combine_images(file_path, output_file, new_size, position, combined_file)

    def browse_files():
        """
        A function that opens a file dialog to select multiple files, and then processes and saves each file using the `process_and_save` method of the `App` class.

        This function does not take any parameters.

        This function does not return any value.
        """
        files = filedialog.askopenfilenames()
        for file in files:
            App.process_and_save(file)

if __name__ == "__main__":
    root = tk.Tk()
    root.deiconify()  # отображение окна

    label = tk.Label(root, text='Выбери файл для конвертации:')
    label.pack()

    button = tk.Button(root, text='ВЫбрать', command=App.browse_files)
    button.pack()
    root.mainloop()