
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

class ImageEditorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Image Editor with PIL")
        self.original_image = None
        self.resized_image = None

        # Buton pentru încărcarea imaginii
        self.load_button = tk.Button(self.master, text="Încarcă imagine", command=self.load_image)
        self.load_button.pack(pady=10)

        # Frame-uri pentru afișarea imaginilor
        self.original_frame = tk.Frame(self.master)
        self.original_frame.pack(side=tk.LEFT, padx=10)
        self.resized_frame = tk.Frame(self.master)
        self.resized_frame.pack(side=tk.RIGHT, padx=10)

    def load_image(self):
        # Deschide o fereastră de dialog pentru selectarea imaginii
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.gif")])
        if file_path:
            self.original_image = Image.open(file_path)
            self.show_images()

    def show_images(self):
        # Redimensionează imaginea la jumătate din dimensiunile originale
        self.resized_image = self.original_image.resize((self.original_image.width // 2, self.original_image.height // 2))

        # Convertim imaginile PIL în imagini tkinter
        original_photo = ImageTk.PhotoImage(self.original_image)
        resized_photo = ImageTk.PhotoImage(self.resized_image)

        # Afișăm imaginea originală
        original_label = tk.Label(self.original_frame, image=original_photo)
        original_label.image = original_photo  # păstrăm o referință pentru a evita ștergerea de către garbage collector
        original_label.pack()

        # Afișăm imaginea redimensionată
        resized_label = tk.Label(self.resized_frame, image=resized_photo)
        resized_label.image = resized_photo  # păstrăm o referință pentru a evita ștergerea de către garbage collector
        resized_label.pack()

def main():
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()

main()
