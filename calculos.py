#import tkinter
#ventana = tkinter.Tk();
#ventana.geometry("600x400")
#etiqueta = tkinter.Label(ventana, text ="Aqui deberia ir mi programa :v", bg="red")
#etiqueta.pack(side =tkinter.LEFT)
#btn1 = tkinter.Button(ventana, text ="Click aqui")
#btn1.pack()
#ventana.mainloop();
import tkinter
ventana = tkinter.Tk()
ventana.geometry("900x600")
ventana.title("Calculo aguinaldo")
#--------------
name_var=tkinter.StringVar()
dui_var=tkinter.StringVar()
nit_var=tkinter.StringVar()
sueldo_var=tkinter.IntVar()
tiempo_var=tkinter.IntVar()

image =  tkinter.PhotoImage(file="unnamed.png")#No soporta archivos Jpg
image =  image.subsample(1,1)#Tamaño
label =  tkinter.Label(image=image)
label.place(x=0, y=0, relwidth=1, relheight=1)

def submit():  
	#hace el calculo del aguinaldo, obtiene las variables de entrada para operarlas
	aguinaldo =""
	aguinaldo_total=""
	var_name = inputNombre.get()
	var_dui = inputDui.get()
	var_nit = inputNit.get()
	var_sueldo = float(inputSueldo.get())
	var_time = int(inputTime.get())
	
	if var_time < 1:
		#no se como sacar una caja flotante tipo alert en JavaScript o promp para capturar otro valor para calcular por dias :c
		aguinaldo = var_sueldo / 30
		aguinaldo_total = aguinaldo * 15
	elif var_time >=1 and var_time <=3:
		aguinaldo = var_sueldo / 30
		aguinaldo_total = aguinaldo * 15
	elif var_time >3 and var_time <=10:
		aguinaldo = var_sueldo / 30
		aguinaldo_total = aguinaldo * 19
	elif var_time >10:
		aguinaldo = var_sueldo / 30
		aguinaldo_total = aguinaldo * 21

	labelData = tkinter.Label(ventana, text = "Información", width = 15, height = 2)
	labelData.grid(row = 6, column = 2)

	labelDataName = tkinter.Label(ventana, text = "Nombre: "+var_name, bg="Navyblue", fg="white", width = 40, height = 2)
	labelDataName.grid(row = 7, column = 2)
	#print(var_name)
	labelDataDui = tkinter.Label(ventana, text = "No DUI: "+var_dui, bg="Navyblue", fg="white", width = 40, height = 2)
	labelDataDui.grid(row = 8, column = 2)
	
	labelDataNit = tkinter.Label(ventana, text = "NIT: "+var_nit, bg="Navyblue", fg="white", width = 40, height = 2)
	labelDataNit.grid(row = 9, column = 2)
	#print(var_name)
	labelDataSueldo = tkinter.Label(ventana, text = f'Sueldo: {var_sueldo}', bg="Navyblue", fg="white", width = 40, height = 2)
	labelDataSueldo.grid(row = 10, column = 2)

	labelDataAguinaldo = tkinter.Label(ventana, text = f'Aguinaldo: {aguinaldo_total}', bg="Navyblue", fg="white", width = 40, height = 2)
	labelDataAguinaldo.grid(row = 11, column = 2)

def clean():
	#Limpia la ventana
	name_var.set("")
	dui_var.set("")
	nit_var.set("")
	sueldo_var.set("")
	#labelDataName.destroy no se como borrar la caja

#------------------------INPUTS----------------------------
inputNombre = tkinter.Entry(ventana, textvariable = name_var, font = "Arial 15", bd=3, relief ="ridge")
inputDui = tkinter.Entry(ventana, textvariable = dui_var, font = "Arial 15", bd=3, relief ="ridge")
inputNit = tkinter.Entry(ventana, textvariable = nit_var, font = "Arial 15", bd=3, relief ="ridge")
inputSueldo = tkinter.Entry(ventana, textvariable = sueldo_var, font = "Arial 15", bd=3, relief ="ridge")
inputTime = tkinter.Entry(ventana, textvariable = tiempo_var, font = "Arial 15", bd=3, relief ="ridge")
#------------------------BOTONES---------------------------
enviar = tkinter.Button(ventana, text = "Enviar", width = 10,bg="Navyblue", fg="white", height = 1,command = submit)
limpiar = tkinter.Button(ventana, text = "Limpiar", width = 10,bg="Navyblue", fg="white", height = 1, command = clean)

#-----------------------LABELS-----------------------------
labelNombre = tkinter.Label(ventana, text = "Nombre: ", bg="Navyblue", fg="white",width = 10, height = 1)
labelDui = tkinter.Label(ventana, text = "DUI: ", bg="Navyblue", fg="white",width = 10, height = 1)
labelNit = tkinter.Label(ventana, text = "NIT: ", bg="Navyblue", fg="white",width = 10, height = 1)
labelSueldo = tkinter.Label(ventana, text = "Sueldo neto: ", bg="Navyblue", fg="white",width = 10, height = 1)
labelTime = tkinter.Label(ventana, text = "Años trabajando: ", bg="Navyblue", fg="white",width = 15, height = 1)

labelIni = tkinter.Label(ventana,text = " ",width = 10, height = 1)
labelSepGrid = tkinter.Label(ventana,text = " ",width = 50, height = 1)

#-----------------------GRILLAS----------------------------
labelIni.grid(row = 0, column = 0)
labelSepGrid.grid(row = 1, column = 3)
labelNombre.grid(row = 1, column = 0)
labelDui.grid(row = 2, column = 0)
labelNit.grid(row = 3, column = 0)
labelSueldo.grid(row = 4, column = 0)
labelTime.grid(row = 5, column = 0)
#----------------------INPUTS------------------------------
inputNombre.grid(row = 1, column = 2)
inputDui.grid(row = 2, column = 2)
inputNit.grid(row = 3, column = 2)
inputSueldo.grid(row = 4, column = 2)
inputTime.grid(row = 5, column = 2)
#----------------------------------------------------------
enviar.grid(row = 1, column = 4)
limpiar.grid(row = 2, column = 4)


ventana.mainloop()


