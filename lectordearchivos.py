from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk,font  # Carga ttk (para widgets nuevos 8.5+)}
from openpyxl import *
#se importa la libreria openpyxl para lectura de archivos excel >= 2010 

class Aplicacion():
    #opciones de la interfaz
    #def __init__(self):
    #    self.raiz = Tk()
    #    self.raiz.title("Lector de archivos")
    #    self.raiz.geometry("1280x600")

    #    self.areatext = ttk.Label(self.raiz, text= "Información").pack(side=TOP)
    #    self.tinfo = Text(self.raiz, width=155, height=33,state=DISABLED).pack(side=TOP)
    #    self.boton1 = ttk.Button(self.raiz, text="Salir", command = quit).pack(side=BOTTOM, fill=BOTH)
    #    self.raiz.mainloop()
    #aqui puede ir el back en otra funcion
    def lectura_archivo(self):
        wb = load_workbook('Algebra relacional.xlsx') #se hace la apertura del archivo
        ws = wb.active #se activa el archivo
        z = 1
        for row in ws.iter_rows(): #este for solo cuenta cuantas filas son
            z += 1
        for col in ws.iter_cols(): #este for es inutil realmente, pero ps idenfica las columnas de NAME y salary
            for cell in col:
                if cell.value == "FIRST_NAME":
                    cmpo = cell.value
                if cell.value == "SALARY":
                    cmpo2 = cell.value
        print(cmpo, cmpo2)
        for x in range (2,z-1): #este for es el que está chido ya que solo recorremos las filas a partir de la 2 
                                #ya que la fila 1 solo es de entidades
            if (int(ws.cell(row=x,column=9).value) >= 10000 and int(ws.cell(row=x,column=9).value) <= 15000) :
                print(ws.cell(row=x,column=3).value, "    " ,ws.cell(row=x,column=9).value)

mi_app = Aplicacion()
mi_app.lectura_archivo()