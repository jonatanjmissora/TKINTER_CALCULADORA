from tkinter import *

root=Tk()
root.title("CALCULADORA")
operacion=""
numero_almacenado=0
resultado=0

#*************** PANTALLA *********************** 
pantalla=StringVar()
visor=Entry(root, textvariable=pantalla, width=20, font=("Arial", 15))
visor.grid(row=1, column=1, padx=5, pady=5, columnspan=5)	#columnspan le digo que ocupe 4 columnas
visor.config(bg="black", fg="#03f943", justify="right")

#*************** FUNC FLOAT_CHECK *********************** 

#*************** FUNC SHOW *********************** 
def show(chr):
	global operacion
	pantalla.set(pantalla.get() + chr)
	
#*************** BORRAR PANTALLA *********************** 
def borrar():
	pantalla.set("")

#*************** FUNC SUMA *********************** 	
def suma():
	global numero_almacenado
	numero_almacenado = "+" + pantalla.get()
	pantalla.set("")
	print(numero_almacenado)

#*************** FUNC RESTA *********************** 	
def resta(num):
	pass

def str_to_num(str):
	
	return 


#*************** FUNC EL_RESULTADO ***********************
def resultado():
	global numero_almacenado
	resultado = str_to_num(pantalla.get()) + str_to_num(numero_almacenado)
	pantalla.set(resultado)
	print(resultado)

#*************** FILA 1 ***********************
Button(root, text="7", width=3, command=lambda:show("7")).grid(row=2, column=1, sticky=W+E)
Button(root, text="8", width=3, command=lambda:show("8")).grid(row=2, column=2, sticky=W+E)
Button(root, text="9", width=3, command=lambda:show("9")).grid(row=2, column=3, sticky=W+E)
Button(root, text="/", width=3)							 .grid(row=2, column=4, sticky=W+E)
Button(root, text="CE", width=3, height=3, command=borrar).grid(row=2, column=5, rowspan=2)

#*************** FILA 2 ***********************
Button(root, text="4", width=3, command=lambda:show("4")).grid(row=3, column=1, sticky=W+E)
Button(root, text="5", width=3, command=lambda:show("5")).grid(row=3, column=2, sticky=W+E)
Button(root, text="6", width=3, command=lambda:show("6")).grid(row=3, column=3, sticky=W+E)
Button(root, text="*", width=3)							 .grid(row=3, column=4, sticky=W+E)

#*************** FILA 3 ***********************
Button(root, text="1", width=3, command=lambda:show("1"))	 	   		.grid(row=4, column=1, sticky=W+E)
Button(root, text="2", width=3, command=lambda:show("2"))	  	   		.grid(row=4, column=2, sticky=W+E)
Button(root, text="3", width=3, command=lambda:show("3"))		   		.grid(row=4, column=3, sticky=W+E)
Button(root, text="-", width=3, command=lambda:resta(pantalla.get()))		.grid(row=4, column=4, sticky=W+E)
Button(root, text="=", width=3, height=3, command=lambda:resultado())		.grid(row=4, column=5, rowspan=2, sticky=W+E)

#*************** FILA 4 ***********************
Button(root, text="0", width=10, command=lambda:show("0")) 		  .grid(row=5, column=1, columnspan= 2, sticky=W+E)
Button(root, text=",", width=3, command=lambda:show("."))		  .grid(row=5, column=3, sticky=W+E)
Button(root, text="+", width=3, command=lambda:suma()).grid(row=5, column=4, sticky=W+E)

root.mainloop()