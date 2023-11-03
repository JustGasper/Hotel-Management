import tkinter as tk
from tkinter import Label,Button,Tk,ttk,messagebox,Entry,Toplevel,Checkbutton
import PIL
from PIL import Image,ImageTk
import Programa_Hotel
import Huespedes
import Insertar_Huesped
import Eliminar_Huesped
from Programa_Hotel import Programa_Hotel
from Insertar_Huesped import Insertar_Huesped_Code
from Huespedes import Huespedes_Informacion_Code
from Eliminar_Huesped import Eliminar_Huesped_Code

def Insertar_Huespeed():
    Ventana_Principal.withdraw()
    Ventana_Ingresar_Huesped.deiconify()

def Cerrar_Ventana_Insertar_Huesped():
    Ventana_Ingresar_Huesped.withdraw()
    Ventana_Principal.deiconify()


def Buscar_Huespedes():
    Ventana_Principal.withdraw()
    Ventana_Buscar_Huespedes.deiconify()

def Cerrar_Ventana_Huesped():
    Ventana_Buscar_Huespedes.withdraw()
    Ventana_Principal.deiconify()



def Eliminar_Huespedes():
    Ventana_Principal.withdraw()
    Ventana_Eliminar_Huespedes.deiconify()


def Cerrar_Ventana_Eliminar_Huesped():
    Ventana_Eliminar_Huespedes.withdraw()
    Ventana_Principal.deiconify()



## ------------------ VENTANA PRINCIPAL AQUÍ ABAJO ---------------- ##
Ventana_Principal = Programa_Hotel()


Ventana_Principal.Boton_Añadir_Usuario.config(command=Insertar_Huespeed)

Ventana_Principal.Boton_Huespedes.config(command=Buscar_Huespedes)

Ventana_Principal.Boton_Eliminar_Huespedes.config(command=Eliminar_Huespedes)
## ------------------ VENTANA PRINCIPAL AQUÍ ARRIBA ---------------- ##







## ------------------ VENTANA INGRESAR HUESPEDES AQUÍ ABAJO ---------------- ##
Ventana_Ingresar_Huesped = Insertar_Huesped_Code()


Ventana_Ingresar_Huesped.Volver_Btn.config(command=Cerrar_Ventana_Insertar_Huesped)


Ventana_Ingresar_Huesped.withdraw()
## ------------------ VENTANA INGRESAR HUESPEDES AQUÍ ARRIBA ---------------- ##





## ------------------ VENTANA BUSCAR HUESPEDES AQUÍ ABAJO ---------------- ##

Ventana_Buscar_Huespedes = Huespedes_Informacion_Code()

Ventana_Buscar_Huespedes.Volver_Btn.config(command=Cerrar_Ventana_Huesped)

Ventana_Buscar_Huespedes.withdraw()
## ------------------ VENTANA BUSCAR HUESPEDES AQUÍ ABAJO ---------------- ##






## ------------------ VENTANA  ELIMINAR HUESPEDES AQUÍ ABAJO ---------------- ##

Ventana_Eliminar_Huespedes = Eliminar_Huesped_Code()

Ventana_Eliminar_Huespedes.Volver_Btn.config(command=Cerrar_Ventana_Eliminar_Huesped)

Ventana_Eliminar_Huespedes.withdraw()
## ------------------ VENTANA ELIMINAR HUESPEDES AQUÍ ABAJO ---------------- ##








Ventana_Principal.Correr_Hotel_Programa()