# Programa: Huespedes!. 
# El mismo consiste, en poder ingresar datos de personas y/o familias, para que puedan reservar y contratar una habitación en el Hotel por X cantidad de tiempo. 
# Todos los datos de los huéspedes (incluyendo habitación donde se hospedan) serán cargados directamente en una base de datos SQLite (por ahora para hacerlo más fácil)
# A su vez. el hotel también cuenta con una base de datos (obviamente) donde se indican cuántas habitaciones hay y qué comidades tienen.
# El programa va a detectar si la habitación está o no está disponible y por cuánto tiempo. 


import tkinter as tk
from tkinter import Label,Button,Tk,ttk,messagebox,Entry,Toplevel
import PIL
from PIL import Image, ImageTk
import pymysql

Conexion = pymysql.connect(host="db4free.net",user="justgasper",password="12345678",db="gasperpruebas")

Cursor=Conexion.cursor()

class Programa_Hotel(Tk):
    def __init__(self,):
        super().__init__()
        self.geometry("1024x720")
        self.title("Hotelería")
        Imagen_1 = Image.open("Imagen_Hotel.jpg")
        Imagen_1 = Imagen_1.resize((1024,720))
        self.Imagen_1 = ImageTk.PhotoImage(Imagen_1)
        self.Imagen_1_label = Label(self,image=self.Imagen_1)
        self.Imagen_1_label.place(x=0,y=0)

        self.Boton_Añadir_Usuario = Button(text="Ingresar Huesped", width=15,height=3,font=("Georgia",15))
        self.Boton_Añadir_Usuario.place(x=425,y=150)

        self.Boton_Huespedes = Button(text="Buscar Huesped", width=15,height=3,font=("Georgia",15))
        self.Boton_Huespedes.place(x=425,y=300)

        self.Boton_Eliminar_Huespedes = Button(text="Eliminar Huesped", width=15,height=3,font=("Georgia",15))
        self.Boton_Eliminar_Huespedes.place(x=425,y=450)


        self.Boton_Salir = Button(text="Salir", width=15,height=3,font=("Georgia",15),command=self.Cerrar_Programa)
        self.Boton_Salir.place(x=825,y=600)

    def Cerrar_Programa(self):
        self.destroy()
    
    def Correr_Hotel_Programa(self):
        self.mainloop()
    
    

# --------------- #      # --------------- #    # --------------- #      # --------------- #    # --------------- #      # --------------- #    # --------------- #      # --------------- #
# --------------- #      # --------------- #    # --------------- #      # --------------- #    # --------------- #      # --------------- #    # --------------- #      # --------------- #
# --------------- #      # --------------- #    # --------------- #      # --------------- #    # --------------- #      # --------------- #    # --------------- #      # --------------- #