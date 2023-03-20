import tkinter as tk
from PIL import Image, ImageTk
import datetime 

# Creación de la ventana principal y su tamaño
ventana = tk.Tk()
ventana.title("Recetario")
ventana.geometry("1000x800")

# Creación de una imagen de fondo usando la librería PIL
imagen_fondo = ImageTk.PhotoImage(Image.open("definitivo.png"))
etiqueta_fondo = tk.Label(ventana, image=imagen_fondo)
etiqueta_fondo.place(x=0, y=0, relwidth=1, relheight=1)

class Recetario:
    def __init__(self,root):
        self.recetas = []
        self.nombre_receta = tk.StringVar()
        self.fecha_creacion= tk.StringVar()
        self.hora_creacion= tk.StringVar()
        self.t_preparacion= tk.StringVar()
        self.t_coccion= tk.StringVar()
        self.ingredientes = []
        self.nombre_ing = tk.StringVar()
        self.cantidad = tk.StringVar()
        self.unidad = tk.StringVar()
        self.procedimiento = []
        self.favorita= tk.BooleanVar()
        fecha = datetime.datetime.now()
        hora = datetime.datetime.now().time()
        

        tk.Label(text="Nombre de receta").grid(row=0, column=0)
        tk.Entry(textvariable=self.nombre_receta).grid(row=0, column=1)

        tk.Label(text="Fecha de creación").grid(row=1, column=0)
        tk.Entry(textvariable=self.fecha_creacion).grid(row=1, column=1)
        self.fecha_creacion.set(fecha.strftime("%d/%m/%Y"))
        
        tk.Label(text="Hora de creación").grid(row=2, column=0)
        tk.Entry(textvariable=self.hora_creacion).grid(row=2, column=1)
        self.hora_creacion.set(hora.strftime("%H:%M"))
        
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
        
        tk.Button(text="Crear receta", command=self.crear).grid(row=11, column=0)
        
        tk.Button(text="Mostrar", command=self.crear).grid(row=11, column=1)
        
        # tk.Button(text="Modificar receta", command=self.modificar).grid(row=11, column=2)
        
        # tk.Button(text="Eliminar receta", command=self.eliminar).grid(row=11, column=3)
        


    def crear(self):
        import json
        from pathlib import Path
        
        ingredientes = Path("mi-GH", "ingredientes.json")
        ingredientes = self.nombre_ing.get(),self.cantidad.get(), self.unidad.get()
        self.ingredientes.append(ingredientes)
        
        recetas= {"nombre_receta":self.nombre_receta.get(),
                "fecha de creacion": self.fecha_creacion.get(),
                "hora de creacion": self.hora_creacion.get(),
                "tiempo de preparacion": self.t_preparacion.get(),
                "tiempo de coccion": self.t_coccion.get(),
                "ingredientes": self.ingredientes,
                "favorita": self.favorita.get()                  
                }
        with open("ingredientes.json", "a") as file:
            json.dump(recetas,file)
            
        # Abre el archivo JSON y carga los datos
        with open("datos.json") as archivo:
            data = json.load(archivo)    
    






if __name__ == "__main__":
    root =tk.Tk()
    app = Recetario(root)
    root.mainloop()
