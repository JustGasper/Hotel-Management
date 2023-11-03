import tkinter as tk
from tkinter import Label,Button,Tk,ttk,messagebox,Entry,Toplevel,Checkbutton
import PIL
from PIL import Image,ImageTk
import pymysql
Conexion = pymysql.connect(host="db4free.net",user="justgasper",password="12345678",db="gasperpruebas")

Cursor=Conexion.cursor()

Cursor.execute("Select Numero_Habitacion from habitaciones")

Habitaciones = Cursor.fetchall()


class Insertar_Huesped_Code(Toplevel):
    def __init__(self,):
        super().__init__()
        self.geometry("1024x720")
        self.title("Ingresar Huesped")

        Imagen_1 = Image.open("Imagen_Ingreso.jpg")
        Imagen_1 = Imagen_1.resize((1024,720))
        self.Imagen_1 = ImageTk.PhotoImage(Imagen_1)
        self.Imagen_1_label = Label(self,image=self.Imagen_1)
        self.Imagen_1_label.place(x=0,y=0)

        self.Nombre_Apellido_Entry = Entry(self,width=30)
        self.Nombre_Apellido_Entry.place(x=210,y=15)
        
        self.DNI_Entry = Entry(self,width=15)
        self.DNI_Entry.place(x=80,y=65)

        self.Desde_Entry = Entry(self,width=10)
        self.Desde_Entry.place(x=80,y=117)

        self.Hasta_Entry = Entry(self,width=10)
        self.Hasta_Entry.place(x=265,y=118)

        self.Cantidad_Familiares_Entry = Entry(self,width=10)
        self.Cantidad_Familiares_Entry.place(x=430,y=165)

        self.Habitaciones_Elegir = ttk.Combobox(self,values=Habitaciones)
        self.Habitaciones_Elegir.place(x=220,y=215)

        self.Num_Celular_Entry = Entry(self,width=15)
        self.Num_Celular_Entry.place(x=220,y=285)

        self.checkbox_CnBlanco_Si_var = tk.IntVar()
        self.Cn_Blanco_CheckList = Checkbutton(self,width=3,height=1,text="Si",font=("Georgia",15),variable=self.checkbox_CnBlanco_Si_var)
        self.Cn_Blanco_CheckList.place(x=140,y=350)

        self.checkbox_CnBlanco_No_var = tk.IntVar()
        self.Cn_Blanco_CheckList_2 = Checkbutton(self,width=3,height=1,text="No",font=("Georgia",15),variable=self.checkbox_CnBlanco_No_var)
        self.Cn_Blanco_CheckList_2.place(x=220,y=350)
        
        self.checkbox_Efectivo_var = tk.IntVar()
        self.Metodo_De_Pago_ChechList = Checkbutton(self,width=6,height=1,text="Efectivo",font=("Georgia",15),variable=self.checkbox_Efectivo_var)
        self.Metodo_De_Pago_ChechList.place(x=180,y=420)

        self.checkbox_Tarjeta_var = tk.IntVar()
        self.Metodo_De_Pago_ChechList_2 = Checkbutton(self,width=6,height=1,text="Tarjeta",font=("Georgia",15),variable=self.checkbox_Tarjeta_var)
        self.Metodo_De_Pago_ChechList_2.place(x=300,y=420)        

        self.checkbox_Afiliado_Si_var = tk.IntVar()
        self.Es_Afiliado_CheckList = Checkbutton(self,width=3,height=1,text="Si",font=("Georgia",15),variable=self.checkbox_Afiliado_Si_var)
        self.Es_Afiliado_CheckList.place(x=130,y=490)
        
        self.checkbox_Afiliado_No_var = tk.IntVar()
        self.Es_Afiliado_CheckList_2 = Checkbutton(self,width=3,height=1,text="No",font=("Georgia",15),variable=self.checkbox_Afiliado_No_var)
        self.Es_Afiliado_CheckList_2.place(x=210,y=490)  
        

        self.Nombre_Apellido_Label = Label(self,text="Nombre y Apellido",width=14,height=1,font=("Georgia",17))
        self.Nombre_Apellido_Label.place(x=-5,y=10)

        self.DNI_Label = Label(self,text="DNI",width=4,height=1,font=("Georgia",17))
        self.DNI_Label.place(x=-8,y=60)

        self.DNI_Guia_Label = Label(self,text="Ingrese el DNI de manera 12-345-678",width=30,height=1,font=("Georgia",14,"italic"))
        self.DNI_Guia_Label.place(x=189,y=60)

        self.Desde_Label = Label(self,text="Desde",width=5,height=1,font=("Georgia",17)) #Desde - Hasta
        self.Desde_Label.place(x=-8,y=110)

        self.Hasta_Label = Label(self,text="Hasta",width=5,height=1,font=("Georgia",17)) #Desde - Hasta
        self.Hasta_Label.place(x=190,y=110)

        self.Cantidad_Familiares_Label = Label(self,text="Cantidad De Familiares/Acompañantes",width=30,height=1,font=("Georgia",17))
        self.Cantidad_Familiares_Label.place(x=-10,y=160)

        self.Habitacion_Label = Label(self,text="Habitación Deseada",width=15,height=1,font=("Georgia",17))
        self.Habitacion_Label.place(x=-6,y=210)

        self.Num_Celular_Label = Label(self,text="Número de Celular:",width=15,height=1,font=("Georgia",17))
        self.Num_Celular_Label.place(x=-8,y=280)

        self.Con_Blanco_Label = Label(self,text="Con Blanco:",width=9,font=("Georgia",17))
        self.Con_Blanco_Label.place(x=-5,y=350)

        self.Metodo_De_Pago_Label = Label(self,text="Método de pago:",width=12,height=1,font=("Georgia",17))
        self.Metodo_De_Pago_Label.place(x=-3,y=420)

        self.Es_Afiliado_Label = Label(self,text="Es Afiliado:",width=8,height=1,font=("Georgia",17))
        self.Es_Afiliado_Label.place(x=0,y=490)

        self.Continuar_Btn = Button(self,text="Ingresar",width=15, height=2,font=("Georgia",13),command=self.Cargar_Huesped)
        self.Continuar_Btn.place(x=830,y=660)

        self.Volver_Btn = Button(self,text="Volver",width=15, height=2,font=("Georgia",13),command=self.Volver_Inicio_Programa)
        self.Volver_Btn.place(x=10,y=660)


    def Cargar_Huesped(self):
            while True:
                Blanco = "A"
                Pago = "A"
                Afiliado = "A"
                Nombre_Apellido_Ingresado = self.Nombre_Apellido_Entry.get()
                DNI_Cargado = self.DNI_Entry.get()
                Desde_Cargado = self.Desde_Entry.get()
                Hasta_Cargado = self.Hasta_Entry.get()
                Cantidad_Huespedes = self.Cantidad_Familiares_Entry.get()
                Habitacion_Deseada = self.Habitaciones_Elegir.get()
                Numero_De_Celular = self.Num_Celular_Entry.get()
                Con_Blanco_Si =  self.checkbox_CnBlanco_Si_var.get()
                Con_Blanco_No =  self.checkbox_CnBlanco_No_var.get()
                Con_Efectivo = self.checkbox_Efectivo_var.get()
                Con_Tarjeta = self.checkbox_Tarjeta_var.get()
                Afiliado_Si = self.checkbox_Afiliado_Si_var.get()
                Afiliado_No = self.checkbox_Afiliado_No_var.get()
                if not (Nombre_Apellido_Ingresado and DNI_Cargado and Desde_Cargado and Hasta_Cargado and Cantidad_Huespedes and Habitacion_Deseada and Numero_De_Celular):
                    messagebox.showerror("Carga de Datos","Las casillas no pueden estar vacías")
                    break
                elif Con_Blanco_Si and Con_Blanco_No and Con_Efectivo and Con_Tarjeta and Afiliado_Si and Afiliado_No:
                    messagebox.showerror("Ingresar","No se puede marcar dos casillas al mismo tiempo, de la misma categoría")
                    break
                elif Con_Blanco_Si==1 and Con_Blanco_No==1:
                    messagebox.showerror("Ingresar","No se puede marcar dos casillas al mismo tiempo, de la misma categoría")
                    break
                elif Con_Efectivo==1 and Con_Tarjeta==1:
                    messagebox.showerror("Ingresar","No se puede marcar dos casillas al mismo tiempo, de la misma categoría")
                    break
                elif Afiliado_Si==1 and Afiliado_No==1:
                    messagebox.showerror("Ingresar","No se puede marcar dos casillas al mismo tiempo, de la misma categoría")
                    break
            
                while True:
                    Contiene_Numeros = False
                    Contiene_Letras = False
                    Nombre_Apellido_Ingresado_Sin_Espacios = Nombre_Apellido_Ingresado.replace(" ","")
                    for caracter_encontrado in Nombre_Apellido_Ingresado_Sin_Espacios:
                        if caracter_encontrado.isnumeric():
                            Contiene_Numeros = True

                    if Contiene_Numeros == False:
                        Primer_Guion = DNI_Cargado.find("-")
                        Segundo_Guion = DNI_Cargado.find("-", Primer_Guion + 1)
                        Extraer_Primer_Guion = DNI_Cargado[Primer_Guion]
                        Extraer_Segundo_Guion = DNI_Cargado[Segundo_Guion]
                        if Extraer_Primer_Guion == "-" and Extraer_Segundo_Guion == "-":
                            Letras_Totales = len(DNI_Cargado)
                            if Letras_Totales == 10:
                                Reemplazo = DNI_Cargado.replace("-","")
                                Nuevas_Letras_Totales = len(Reemplazo)
                                if Nuevas_Letras_Totales == 8:
                                    for caracter_encontrado in Reemplazo:
                                        if caracter_encontrado.isalpha():
                                            Contiene_Letras = True
                                    if Contiene_Letras == False:
                                        Primera_Barra_Desde_Cargado = Desde_Cargado.find("/")
                                        Segunda_Barra_Desde_Cargado = Desde_Cargado.find("/", Primera_Barra_Desde_Cargado + 1)
                                        Extraer_Primera_Barra = Desde_Cargado[Primera_Barra_Desde_Cargado]
                                        Extraer_Segunda_Barra = Desde_Cargado[Segunda_Barra_Desde_Cargado]
                                        if Extraer_Primera_Barra == "/" and Extraer_Segunda_Barra == "/":
                                            Desde_Cargado_Sin_Guion = Desde_Cargado.replace("/","")
                                            for caracter_encontrado in Desde_Cargado_Sin_Guion:
                                                if caracter_encontrado.isalpha():
                                                    Contiene_Letras = True
                                            if Contiene_Letras == False:
                                                Primera_Barra_Hasta_Cargado = Hasta_Cargado.find("/")
                                                Segunda_Barra_Hasta_Cargado = Hasta_Cargado.find("/", Primera_Barra_Hasta_Cargado + 1)
                                                Extraer_Primera_Barra_Hasta_Cargado = Hasta_Cargado[Primera_Barra_Hasta_Cargado]
                                                Extraer_Segunda_Barra_Hasta_Cargado = Hasta_Cargado[Segunda_Barra_Hasta_Cargado]
                                                if Extraer_Primera_Barra_Hasta_Cargado == "/" and Extraer_Segunda_Barra_Hasta_Cargado == "/":
                                                    Hasta_Cargado_Sin_Guion = Hasta_Cargado.replace("/","")
                                                    for caracter_encontrado in Hasta_Cargado_Sin_Guion:
                                                        if caracter_encontrado.isalpha():
                                                            Contiene_Letras = True
                                                    if Contiene_Letras == False:
                                                        for caracter_encontrado in Numero_De_Celular:
                                                            if caracter_encontrado.isalpha():
                                                                Contiene_Letras = True
                                                        if Contiene_Letras == False:
                                                            Cursor.execute("Select Disponible From habitaciones WHERE Numero_Habitacion = %s",(Habitacion_Deseada,))
                                                            Habitacion_Disponible = Cursor.fetchone()
                                                            Lista = [Habitacion_Disponible]
                                                            Extraer_D_Lista = Lista[0]
                                                            Convertir_A_TXT = str(Extraer_D_Lista)
                                                            Extraer_Letra = Convertir_A_TXT[2]
                                                            if Extraer_Letra == "S":
                                                                Cursor.execute("INSERT INTO huespedes (Nombre_Apellido,DNI,Fecha_Ingreso,Fecha_Salida,Acompaniantes,Habitacion_Hospedaje,Celular,Cn_Blanco,Metodo_Pago,Afiliado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" , (Nombre_Apellido_Ingresado,DNI_Cargado,Desde_Cargado,Hasta_Cargado,Cantidad_Huespedes,Habitacion_Deseada,Numero_De_Celular,Blanco,Pago,Afiliado))
                                                                Conexion.commit()
                                                                if Con_Blanco_Si==1:
                                                                    Cursor.execute("UPDATE huespedes SET Cn_Blanco='Si' WHERE DNI = %s" ,(DNI_Cargado,))
                                                                if Con_Blanco_No==1:
                                                                    Cursor.execute("UPDATE huespedes SET Cn_Blanco='No' WHERE DNI = %s" ,(DNI_Cargado,))
                                                                if Con_Efectivo==1:
                                                                    Cursor.execute("UPDATE huespedes SET Metodo_Pago='Efectivo' WHERE DNI = %s" ,(DNI_Cargado,))
                                                                if Con_Tarjeta==1:
                                                                    Cursor.execute("UPDATE huespedes SET Metodo_Pago='Tarjeta' WHERE DNI = %s" ,(DNI_Cargado,))
                                                                if Afiliado_Si==1:
                                                                    Cursor.execute("UPDATE huespedes SET Afiliado='Si' WHERE DNI = %s" ,(DNI_Cargado,))
                                                                if Afiliado_No==1:
                                                                    Cursor.execute("UPDATE huespedes SET Afiliado='No' WHERE DNI = %s" ,(DNI_Cargado,))
                                                                self.Nombre_Apellido_Entry.delete(0,tk.END)
                                                                self.DNI_Entry.delete(0,tk.END)
                                                                self.Desde_Entry.delete(0,tk.END)
                                                                self.Hasta_Entry.delete(0,tk.END)
                                                                self.Cantidad_Familiares_Entry.delete(0,tk.END)
                                                                self.Num_Celular_Entry.delete(0, tk.END)
                                                                self.Cn_Blanco_CheckList.deselect()
                                                                self.Cn_Blanco_CheckList_2.deselect()
                                                                self.Metodo_De_Pago_ChechList.deselect()
                                                                self.Metodo_De_Pago_ChechList_2.deselect()
                                                                self.Es_Afiliado_CheckList.deselect()
                                                                self.Es_Afiliado_CheckList_2.deselect()
                                                                Conexion.commit()
                                                                messagebox.showinfo("Estadia","Su estadia se estableció correctamente!")
                                                                Cursor.execute("UPDATE habitaciones SET Disponible='N' WHERE Numero_Habitacion = %s" ,(Habitacion_Deseada,))
                                                                Conexion.commit()
                                                                break     
                                                            else:
                                                                messagebox.showwarning("Habitación","Esta habitación ya se encuentra ocupada, por favor, solicite otra")
                                                                break
                                                        else:
                                                            messagebox.showerror("Inscripción","Usted ingresó datos inválidos 10")
                                                            Numero_De_Celular = None
                                                            self.Num_Celular_Entry.delete(0,tk.END)
                                                            break
                                                    else:
                                                        messagebox.showerror("Inscripción","Usted ingresó datos inválidos 9")
                                                        Hasta_Cargado = None
                                                        self.Hasta_Entry.delete(0,tk.END)
                                                        break
                                                else:
                                                    messagebox.showerror("Inscripción","Usted ingresó datos inválidos 8")
                                                    Hasta_Cargado = None
                                                    self.Hasta_Entry.delete(0,tk.END)
                                                    break
                                            else:
                                                messagebox.showerror("Inscripción","Usted ingresó datos inválidos 7")
                                                Desde_Cargado = None
                                                self.Desde_Entry.delete(0,tk.END)
                                                break
                                        else:
                                            messagebox.showerror("Inscripción","Usted ingresó datos inválidos 6")
                                            Desde_Cargado = None
                                            self.Desde_Entry.delete(0,tk.END)
                                            break
                                    else:
                                        messagebox.showerror("Inscripción","Usted ingresó datos inválidos 5")
                                        DNI_Cargado = None
                                        self.DNI_Entry.delete(0,tk.END)
                                        break 
                                else:
                                    messagebox.showerror("Inscripción","Usted ingresó datos inválidos 4")
                                    DNI_Cargado = None
                                    self.DNI_Entry.delete(0,tk.END)
                                    break  
                            else:
                                messagebox.showerror("Inscripción","Usted ingresó datos inválidos 3")
                                DNI_Cargado = None
                                self.DNI_Entry.delete(0,tk.END)
                                break
                        else:
                            messagebox.showerror("Inscripción","Usted ingresó datos inválidos 2")
                            DNI_Cargado = None
                            self.DNI_Entry.delete(0,tk.END)
                            break
                    else:
                        messagebox.showerror("Inscripción","Usted ingresó datos inválidos 1")
                        Nombre_Apellido_Ingresado = None
                        Nombre_Apellido_Ingresado_Sin_Espacios = None
                        self.Nombre_Apellido_Entry.delete(0,tk.END)
                        break
                break
             

    def Iniciar_Progr(self):
        self.mainloop()

    def Volver_Inicio_Programa(self):
        self.withdraw()

    


# --------------- #      # --------------- #    # --------------- #      # --------------- #    # --------------- #      # --------------- #    # --------------- #      # --------------- #
# --------------- #      # --------------- #    # --------------- #      # --------------- #    # --------------- #      # --------------- #    # --------------- #      # --------------- #
# --------------- #      # --------------- #    # --------------- #      # --------------- #    # --------------- #      # --------------- #    # --------------- #      # --------------- #
