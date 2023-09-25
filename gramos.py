from tkinter import Tk, Label, Button,Entry, Frame, END
import pandas as pd

ventana = Tk()
ventana.config(bg='black')
ventana.geometry('560x388')
ventana.resizable(0,0)
ventana.title('Guardar datos en Excel')
nombre1,apellido1,edad1,correo1 = [],[],[],[]

def agregar_datos():
	global nombre1, apellido1, correo1

	nombre1.append(ingresa_nombre.get())
	apellido1.append(ingresa_apellido.get())
	edad1.append(ingresa_edad.get())
	correo1.append(ingresa_correo.get())


	ingresa_nombre.delete(0,END)
	ingresa_apellido.delete(0,END)
	ingresa_edad.delete(0,END)
	ingresa_correo.delete(0,END)

def guardar_datos():	
	global nombre1,apellido1,edad1,correo1
	datos = {'Nombre Ic':nombre1,'Cofre':apellido1, 'Cantidad Guardada':edad1, 'Cantidad Total':correo1} 
	nom_excel  = str(nombre_archivo.get() + ".xlsx")	
	df = pd.DataFrame(datos,columns =  ['Nombre Ic', 'Cofre', 'Cantidad Guardada', 'Cantidad Total']) 
	df.to_excel(nom_excel)
	nombre_archivo.delete(0,END)

frame1 = Frame(ventana, bg='#FFF5E4')
frame1.grid(column=0, row=0, sticky='nsew')
frame2 = Frame(ventana, bg='#FFC4C4')
frame2.grid(column=1, row=0, sticky='nsew')

nombre = Label(frame1, text ='Nombre Ic', width=12, bg='#FFC4C4').grid(column=0, row=0, pady=30, padx= 0)
ingresa_nombre = Entry(frame1,  width=19, font = ('Arial',12),highlightbackground = "#FFC4C4", highlightthickness=4)
ingresa_nombre.grid(column=1, row=0)

apellido = Label(frame1, text ='Cofre', width=10, bg='#FFC4C4').grid(column=0, row=1, pady=30, padx= 10)
ingresa_apellido = Entry(frame1, width=19, font = ('Arial',12),highlightbackground = "#FFC4C4", highlightthickness=4)
ingresa_apellido.grid(column=1, row=1)

edad = Label(frame1, text ='Cantidad Guardada', width=14, bg='#FFC4C4').grid(column=0, row=2, pady=30, padx= 10)
ingresa_edad = Entry(frame1,  width=19, font = ('Arial',12),highlightbackground = "#FFC4C4", highlightthickness=4)
ingresa_edad.grid(column=1, row=2)

correo = Label(frame1, text ='Cantidad Total', width=12, bg='#FFC4C4').grid(column=0, row=3, pady=30, padx= 10)
ingresa_correo = Entry(frame1,  width=19, font = ('Arial',12),highlightbackground = "#FFC4C4", highlightthickness=4)
ingresa_correo.grid(column=1, row=3)

agregar = Button(frame1, width=20, font = ('Arial',12, 'bold'), text='Agregar', bg='#FFF5E4',bd=5, command =agregar_datos)
agregar.grid(columnspan=2, row=5, pady=20, padx= 10)

archivo = Label(frame2, text ='Ingrese Nombre del archivo', width=25, bg='#FFF5E4',font = ('Arial',12, 'bold'), fg='black')
archivo.grid(column=0, row=0, pady=10, padx= 10)

nombre_archivo = Entry(frame2, width=23, font = ('Arial',12),highlightbackground = "#FFF5E4", highlightthickness=4)
nombre_archivo.grid(column=0, row=1, pady=1, padx= 10)

guardar = Button(frame2, width=20, font = ('Arial',12, 'bold'), text='Guardar', bg='#EE6983',bd=5, command =guardar_datos)
guardar.grid(column=0, row=2, pady=20, padx= 10)
ventana.mainloop()
