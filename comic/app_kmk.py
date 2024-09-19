import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

img = Image.open("comic.png")

# Obtener las dimensiones de la imagen
width, height = img.size



root = tk.Tk()
root.title("")
root.resizable(0, 0)
root.geometry(f"{width}x{height}")
root.config(bg="#2c3e50")
root.attributes("-topmost", True)

image = Image.open("comic.png")  # Abre la imagen desde el archivo

# Convertir la imagen para que Tkinter la entienda
photo = ImageTk.PhotoImage(image)  # Pasa el objeto 'image' aquí, no el nombre del archivo

# Crear un Label para mostrar la imagen
label = tk.Label(root, image=photo)
label.pack()


root.mainloop()