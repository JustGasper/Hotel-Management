import tkinter as tk
from tkinter import Label,Button,ttk,messagebox,Entry,Toplevel,Tk
import PIL
from PIL import Image,ImageTk
import pymysql

Conexion = pymysql.connect(host="db4free.net",user="justgasper",password="12345678",db="gasperpruebas")

Cursor=Conexion.cursor()

Cursor.execute("Select Numero_Habitacion from habitaciones")

Habitaciones = Cursor.fetchall()



class Eliminar_Huesped_Code(Toplevel):

    def __init__(self,):
        super().__init__()
        self.geometry("1024x720")
        self.title("Huespedes")

        Imagen_1 = Image.open("Imagen_Eliminacion.jpg")
        Imagen_1 = Imagen_1.resize((1024,720))
        self.Imagen_1 = ImageTk.PhotoImage(Imagen_1)
        self.Imagen_1_label = Label(self,image=self.Imagen_1)
        self.Imagen_1_label.place(x=0,y=0)

        self.Ingrese_Nombre_Label = Label(self,text="Ingrese Nombre y Apellido o sino DNI",width=30,height=1,font=("Georgia",14,"italic"))
        self.Ingrese_Nombre_Label.place(x=120,y=4)

        self.Boton_Elegir = Button(self,text="Buscar",width=10,height=1, command=self.Buscar_Huesped)
        self.Boton_Elegir.place(x=500,y=35)

        self.Buscar_Huesped_Entry = Entry(self,width=25)
        self.Buscar_Huesped_Entry.place(x=465,y=10)



        self.Informacion_Huesped_Label = Label(self, text="Información sobre el Huesped", width=25,height=1,font=("Georgia",17,"italic"))
        self.Informacion_Huesped_Label.place(x=350,y=70)

        self.Nombre_Completo_Label = Label(self,text="Nombre y Apellido:",width=16,height=1,font=("Georgia",14,"italic"))
        self.Nombre_Completo_Label.place(x=-4,y=150)

        self.DNI_Huesped_Label = Label(self,text="DNI:",width=5,height=1,font=("Georgia",14,"italic"))
        self.DNI_Huesped_Label.place(x=50,y=210) 

        self.Cantidad_Acompañantes_Label = Label(self,text="Cantidad de Acompañantes:",width=23,height=1,font=("Georgia",14,"italic"))
        self.Cantidad_Acompañantes_Label.place(x=-7,y=270) 

        self.Habitacion_Que_Hospeda_Label = Label(self,text="Habitación en la que se hospeda:",width=27,height=1,font=("Georgia",14,"italic"))
        self.Habitacion_Que_Hospeda_Label.place(x=-8,y=370) 


        self.Ingreso_Desde_Label = Label(self,text="Ingresó en la fecha:", width=15,height=1,font=("Georgia",14,"italic"))
        self.Ingreso_Desde_Label.place(x=0,y=430)

        self.Retira_Huesped_Label = Label(self,text="Se retira en la fecha:",width=18,height=1,font=("Georgia",14,"italic"))
        self.Retira_Huesped_Label.place(x=-11,y=490)

        self.Celular_Huesped_Label = Label(self,text="Celular del Huesped:",width=18,height=1,font=("Georgia",14,"italic"))
        self.Celular_Huesped_Label.place(x=-13,y=550)



        self.Nombre_Completo_2_Label = Label(self,text=" ",width=20,height=1,font=("Georgia",14,"italic"))
        self.Nombre_Completo_2_Label.place(x=200,y=150)

        self.DNI_Huesped_2_Label = Label(self,text=" ",width=12,height=1,font=("Georgia",14,"italic"))
        self.DNI_Huesped_2_Label.place(x=200,y=210)

        self.Cantidad_Acompañantes_2_Label = Label(self,text=" ",width=3,height=1,font=("Georgia",14,"italic"))
        self.Cantidad_Acompañantes_2_Label.place(x=250,y=270)

        self.Habitacion_Que_Hospeda_2_Label = Label(self,text=" ",width=3,height=1,font=("Georgia",14,"italic"))
        self.Habitacion_Que_Hospeda_2_Label.place(x=290,y=370) 

        self.Ingreso_Desde_2_Label = Label(self,text=" ", width=11,height=1,font=("Georgia",14,"italic"))
        self.Ingreso_Desde_2_Label.place(x=200,y=430)

        self.Retira_Huesped_2_Label = Label(self,text=" ",width=11,height=1,font=("Georgia",14,"italic"))
        self.Retira_Huesped_2_Label.place(x=200,y=490)

        self.Celular_Huesped_2_Label = Label(self,text=" ",width=18,height=1,font=("Georgia",14,"italic"))
        self.Celular_Huesped_2_Label.place(x=200,y=550)

        self.Volver_Btn = Button(self, text="Volver",width=15, height=2,font=("Georgia",13),command=self.Volver_Inicio_Programa)
        self.Volver_Btn.place(x=10,y=660)




    def Buscar_Huesped(self):
        Palabras_True = False
        Numeros_True = False
        Huesped_Deseado =  self.Buscar_Huesped_Entry.get()
        if Huesped_Deseado == "":
            messagebox.showerror("Busqueda","No ha ingresado ningún dato")
        else:
            Huesped_Deseado_Sin_Espacios = Huesped_Deseado.replace(" ","")
            Huesped_Deseado_Sin_Guiones = Huesped_Deseado.replace("-","")
            for Caracter_Extraido in Huesped_Deseado_Sin_Espacios:
                if Caracter_Extraido.isnumeric():
                    Numeros_True = True
            
            for Caracter_Extraido in Huesped_Deseado_Sin_Guiones:
                if Caracter_Extraido.isalpha():
                    Palabras_True = True
        

            if Numeros_True == False:
                Cursor.execute("Select * from huespedes WHERE Nombre_Apellido = %s" ,(Huesped_Deseado,))
                Resultado = Cursor.fetchone()
                if Resultado == None:
                    messagebox.showerror("Error","No existe un huesped con este nombre")
                else:
                    self.Nombre_Completo_2_Label.config(text=Resultado[1],font=("Georgia",14,"italic"),bg="#F0F0F0")
                    self.Cantidad_Acompañantes_2_Label.config(text=Resultado[5],font=("Georgia",14,"italic"),bg="#F0F0F0")
                    self.DNI_Huesped_2_Label.config(text=Resultado[2],font=("Georgia",14,"italic"),bg="#F0F0F0")
                    self.Ingreso_Desde_2_Label.config(text=Resultado[3],font=("Georgia",14,"italic"),bg="#F0F0F0")
                    self.Retira_Huesped_2_Label.config(text=Resultado[4],font=("Georgia",14,"italic"),bg="#F0F0F0")
                    self.Celular_Huesped_2_Label.config(text=Resultado[7],font=("Georgia",14,"italic"),bg="#F0F0F0")
                    self.Habitacion_Que_Hospeda_2_Label.config(text=Resultado[6],font=("Georgia",14,"italic"),bg="#F0F0F0")
                    Eliminar = messagebox.askyesno("Eliminar","¿Desea Eliminar este Huesped de la Base de Datos?")
                    if Eliminar == 1:
                        Habitacion_Ocupada = Resultado[6]
                        Cursor.execute("UPDATE habitaciones SET Disponible='S' WHERE Disponible='N' and Numero_Habitacion = %s" ,(Habitacion_Ocupada,))
                        Conexion.commit()
                        Cursor.execute("DELETE from huespedes WHERE Nombre_Apellido = %s" ,(Huesped_Deseado,))
                        Conexion.commit()
                        messagebox.showinfo("Eliminar","Se ha eliminado con éxito al Hueped de la Base De Datos. Que tenga un muy buen día!")
                        self.Nombre_Completo_2_Label.config(text="",bg="#F0F0F0")
                        self.Cantidad_Acompañantes_2_Label.config(text="",bg="#F0F0F0")
                        self.DNI_Huesped_2_Label.config(text="",bg="#F0F0F0")
                        self.Ingreso_Desde_2_Label.config(text="",bg="#F0F0F0")
                        self.Retira_Huesped_2_Label.config(text="",bg="#F0F0F0")
                        self.Celular_Huesped_2_Label.config(text="",bg="#F0F0F0")
                        self.Habitacion_Que_Hospeda_2_Label.config(text="",bg="#F0F0F0")
                    else:
                        messagebox.showinfo("Eliminar","Usted NO ha eliminado a nadie. Que tenga un buen día!")
                
            else:
                if Palabras_True == False:
                    Cursor.execute("Select * from huespedes WHERE DNI = %s" ,(Huesped_Deseado,))
                    Resultado = Cursor.fetchone()
                    if Resultado == None:
                        messagebox.showerror("Error","No existe un huesped con este DNI")
                    else:
                        self.Nombre_Completo_2_Label.config(text=Resultado[1],font=("Georgia",14,"italic"),bg="#F0F0F0")
                        self.Cantidad_Acompañantes_2_Label.config(text=Resultado[5],font=("Georgia",14,"italic"),bg="#F0F0F0")
                        self.DNI_Huesped_2_Label.config(text=Resultado[2],font=("Georgia",14,"italic"),bg="#F0F0F0")
                        self.Ingreso_Desde_2_Label.config(text=Resultado[3],font=("Georgia",14,"italic"),bg="#F0F0F0")
                        self.Retira_Huesped_2_Label.config(text=Resultado[4],font=("Georgia",14,"italic"),bg="#F0F0F0")
                        self.Celular_Huesped_2_Label.config(text=Resultado[7],font=("Georgia",14,"italic"),bg="#F0F0F0")
                        self.Habitacion_Que_Hospeda_2_Label.config(text=Resultado[6],font=("Georgia",14,"italic"),bg="#F0F0F0")
                        Eliminar = messagebox.askyesno("Eliminar","¿Desea Eliminar este Huesped de la Base de Datos?")
                        if Eliminar == 1:
                            Habitacion_Ocupada = Resultado[6]
                            Cursor.execute("UPDATE habitaciones SET Disponible='S' WHERE Disponible='N' and Numero_Habitacion = %s" ,(Habitacion_Ocupada,))
                            Conexion.commit()
                            Cursor.execute("DELETE from huespedes WHERE DNI = %s" ,(Huesped_Deseado,))
                            Conexion.commit()
                            messagebox.showinfo("Eliminar","Se ha eliminado con éxito al Hueped de la Base De Datos. Que tenga un muy buen día!")
                            self.Nombre_Completo_2_Label.config(text="",bg="#F0F0F0")
                            self.Cantidad_Acompañantes_2_Label.config(text="",bg="#F0F0F0")
                            self.DNI_Huesped_2_Label.config(text="",bg="#F0F0F0")
                            self.Ingreso_Desde_2_Label.config(text="",bg="#F0F0F0")
                            self.Retira_Huesped_2_Label.config(text="",bg="#F0F0F0")
                            self.Celular_Huesped_2_Label.config(text="",bg="#F0F0F0")
                            self.Habitacion_Que_Hospeda_2_Label.config(text="",bg="#F0F0F0")
                        else:
                            messagebox.showinfo("Eliminar","Usted NO ha eliminado a nadie. Que tenga un buen día!")


    def Volver_Inicio_Programa(self):
        self.withdraw()

        
    def Abrir_App(self):
        self.mainloop()

# --------------- #      # --------------- #    # --------------- #      # --------------- #    # --------------- #      # --------------- #    # --------------- #      # --------------- #
# --------------- #      # --------------- #    # --------------- #      # --------------- #    # --------------- #      # --------------- #    # --------------- #      # --------------- #
# --------------- #      # --------------- #    # --------------- #      # --------------- #    # --------------- #      # --------------- #    # --------------- #      # --------------- #
