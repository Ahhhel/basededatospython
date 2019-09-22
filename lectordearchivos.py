from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk,font  # Carga ttk (para widgets nuevos 8.5+)}

class Aplicacion():
    #opciones de la interfaz
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Lector de archivos")
        self.raiz.geometry("1280x600")

        self.areatext = ttk.Label(self.raiz, text= "Información").pack(side=TOP)
        self.tinfo = Text(self.raiz, width=155, height=33).pack(side=TOP)
        self.boton1 = ttk.Button(self.raiz, text="Salir", command = quit).pack(side=BOTTOM, fill=BOTH)
        self.raiz.mainloop()
    #aqui puede ir el back en otra funcion

def main():
    mi_app= Aplicacion()
    return 0


if __name__ == '__main__':
    main()  