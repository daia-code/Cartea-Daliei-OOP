from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

class ImagePixelEditorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Image Pixel Editor with PIL")
        self.original_image = None
        self.modified_image = None

        # Buton pentru încărcarea imaginii
        self.load_button = tk.Button(self.master, text="Încarcă imagine", command=self.load_image)
        self.load_button.pack(pady=10)

        # Frame-uri pentru afișarea imaginilor
        self.original_frame = tk.Frame(self.master)
        self.original_frame.pack(side=tk.LEFT, padx=10)
        self.modified_frame = tk.Frame(self.master)
        self.modified_frame.pack(side=tk.RIGHT, padx=10)

    def load_image(self):
        # Deschide o fereastră de dialog pentru selectarea imaginii
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.gif")])
        if file_path:
            self.original_image = Image.open(file_path)
            self.modify_image()

    def modify_image(self):
        # Creează o copie a imaginii originale pentru a modifica pixelii
        self.modified_image = self.original_image.copy()

        # Obține dimensiunile imaginii
        width, height = self.modified_image.size

        # Parcurge fiecare pixel și inversăm culorile
        for x in range(width):
            for y in range(height):
                current_color = self.modified_image.getpixel((x, y))
                # Inversăm culorile (255 - valoarea fiecărui canal RGB)
                new_color = tuple(255 - value for value in current_color)
                self.modified_image.putpixel((x, y), new_color)

        # Convertim imaginile PIL în imagini tkinter
        original_photo = ImageTk.PhotoImage(self.original_image)
        modified_photo = ImageTk.PhotoImage(self.modified_image)

        # Afișăm imaginea originală
        original_label = tk.Label(self.original_frame, image=original_photo)
        original_label.image = original_photo  # păstrăm o referință pentru a evita ștergerea de către garbage collector
        original_label.pack()

        # Afișăm imaginea modificată
        modified_label = tk.Label(self.modified_frame, image=modified_photo)
        modified_label.image = modified_photo  # păstrăm o referință pentru a evita ștergerea de către garbage collector
        modified_label.pack()

root = tk.Tk()
app = ImagePixelEditorApp(root)
root.mainloop()


