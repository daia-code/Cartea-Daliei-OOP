from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

class ImageEditorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Image Editor with PIL")
        self.original_image = None
        self.edited_image = None

        # Buton pentru încărcarea imaginii
        self.load_button = tk.Button(self.master, text="Încarcă imagine", command=self.load_image)
        self.load_button.pack(pady=10)

        # Frame-uri pentru afișarea imaginilor
        self.original_frame = tk.Frame(self.master)
        self.original_frame.pack(side=tk.LEFT, padx=10)
        self.edited_frame = tk.Frame(self.master)
        self.edited_frame.pack(side=tk.RIGHT, padx=10)

    def load_image(self):
        # Deschide o fereastră de dialog pentru selectarea imaginii
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.gif")])
        if file_path:
            self.original_image = Image.open(file_path)
            self.show_images()

    def show_images(self):
        # Convertim imaginea în alb-negru
        self.edited_image = self.original_image.convert("L")

        # Convertim imaginile PIL în imagini tkinter
        original_photo = ImageTk.PhotoImage(self.original_image)
        edited_photo = ImageTk.PhotoImage(self.edited_image)

        # Afișăm imaginea originală
        original_label = tk.Label(self.original_frame, image=original_photo)
        original_label.image = original_photo  # păstrăm o referință pentru a evita ștergerea de către garbage collector
        original_label.pack()

        # Afișăm imaginea editată (alb-negru)
        edited_label = tk.Label(self.edited_frame, image=edited_photo)
        edited_label.image = edited_photo  # păstrăm o referință pentru a evita ștergerea de către garbage collector
        edited_label.pack()

def main():
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()

main()
