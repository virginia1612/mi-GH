import tkinter as tk
from PIL import Image, ImageTk
import json


class Recetario:
    def __init__(self,root):

        self.nombre_receta = tk.StringVar()
        self.fecha_creacion= tk.StringVar()
        self.hora_creacion= tk.StringVar()
        self.t_preparacion= tk.StringVar()
        self.t_coccion= tk.StringVar()
        self.ingredientes = []
        self.nombre_ing = tk.StringVar()
        self.cantidad = tk.StringVar()
        self.unidad = tk.StringVar()
        self.favorita= tk.BooleanVar()
        self.root = root
        self.root.title("Recetario")
        self.root.geometry("1000x800")
        
        ingredientes = self.nombre_ing.get(),self.cantidad.get(), self.unidad.get()
        self.ingredientes.append(ingredientes)

        tk.Label(text="Nombre de receta").grid(row=0, column=0)
        tk.Entry(textvariable=self.nombre_receta).grid(row=0, column=1)

        tk.Label(text="Fecha de creación").grid(row=1, column=0)
        tk.Entry(textvariable=self.fecha_creacion).grid(row=1, column=1)
        
        tk.Label(text="Hora de creación").grid(row=2, column=0)
        tk.Entry(textvariable=self.hora_creacion).grid(row=2, column=1)
        
        tk.Label(text="Tiempo de preparación").grid(row=3, column=0)
        tk.Entry(textvariable=self.t_preparacion).grid(row=3, column=1)
        
        tk.Label(text="Tiempo de cocción").grid(row=4, column=0)
        tk.Entry(textvariable=self.t_coccion).grid(row=4, column=1)
        
        tk.Label(text= "Ingredientes").grid(row=5, column=0)
        tk.Label(text="Nombre").grid(row=6, column=0)
        tk.Entry(textvariable=self.nombre_ing).grid(row=6, column=1)

        tk.Label(text="Cantidad").grid(row=7, column=0)
        tk.Entry(textvariable=self.cantidad).grid(row=7, column=1)

        tk.Label(text="Unidad").grid(row=8, column=0)
        tk.Entry(textvariable=self.unidad).grid(row=8, column=1)
        
        tk.Label(text="Favorita").grid(row=9, column=0)
        tk.Checkbutton(textvariable=self.favorita).grid(row=9, column=1)
        
        tk.Button(text="Agregar", command=self.agregar).grid(row=11, column=0)
        tk.Button(text="Mostrar", command=self.mostrar).grid(row=11, column=1)


    def agregar(self):
        import json
        with open("ingredientes.json", "a") as file:
            self.ingredientes.append({"nombre": self.nombre.get(), "cantidad": self.cantidad.get(), "unidad": self.unidad.get()})
            json.dump(self.ingredientes, file)

    def mostrar(self):
        import json
        with open("ingredientes.json", "r") as file:
            self.ingredientes = json.load(file)
            print(self.ingredientes)
            for ingrediente in self.ingredientes:
                print(ingrediente["nombre"], ingrediente["cantidad"], ingrediente["unidad"])



if __name__ == "__main__":
    root =tk.Tk()
    app = Recetario(root)
    root.mainloop()
