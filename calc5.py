from tkinter import *

#================================================================
# Calculadora simple para manejar conceptos de Python y Tkinter
#================================================================

# arreglar problemas de ingreso de caracteres incorrectos
# arreglar problemas de 0 adelante
# arreglar problemas de ingreso de operaciones sin numeros
# pantalla en 0 cuando se borra o se ingresa 2do numero
# arreglar operaciones acumulativas apretando =
# arreglar problema de multiples "."
# programar el ingreso del teclado (bind)
# ver que pasa con numero negativos
# estetica GUI
# poner separacione de miles y millones
# bloquerar ventana
# modificar a frame
# estetica de codigo

#*************** CONSTANTES y VARIABLES *******************
operacion=""
numero_almacenado=0
resultado=0
fnt = ("Arial", 15)

#*************** FUNC FLOAT_CHECK *************************
def float_check(num):
	if num-int(num)>0:
		return num
	else:
		return int(num)

#*************** FUNC SHOW ********************************
def show(chr):
	global operacion
	pantalla.set(pantalla.get() + chr)
	
#*************** BORRAR PANTALLA **************************
def borrar():
	pantalla.set("")

#*************** FUNC SUMA ********************************	
def suma():
	global numero_almacenado
	numero_almacenado = "+" + pantalla.get()
	pantalla.set("")

#*************** FUNC RESTA *******************************
def resta():
	global numero_almacenado
	numero_almacenado = "-" + pantalla.get()
	pantalla.set("")

#*************** FUNC MULTI ******************************* 	
def multi():
	global numero_almacenado
	numero_almacenado = "*" + pantalla.get()
	pantalla.set("")

#*************** FUNC DIV ********************************* 	
def divi():
	global numero_almacenado
	numero_almacenado = "/" + pantalla.get()
	pantalla.set("")

#*************** FUNC EL_RESULTADO ************************
def resultado():
	global numero_almacenado
	print(numero_almacenado)
	operacion = numero_almacenado[0]
	if operacion == "+":
		resultado = int(pantalla.get()) + int(numero_almacenado[1:])
	elif operacion == "-":
		resultado = int(numero_almacenado[1:]) - int(pantalla.get())
	elif operacion == "*":
		resultado = int(numero_almacenado[1:]) * int(pantalla.get())
	elif operacion == "/":
		resultado = int(numero_almacenado[1:]) / int(pantalla.get())
	pantalla.set(float_check(resultado))
	
root=Tk()
root.title("CALCULADORA")
root.geometry("345x360+1000+50")
root.resizable(False, False)
win = Frame(root)
win.grid(row=0, column=0, padx=10, pady=10)

#*************** PANTALLA *********************************
pantalla=StringVar()
visor=Entry(win, textvariable=pantalla, width=12, font=("Arial", 35))
visor.grid(row=0, column=0, pady=10, columnspan=5)
visor.config(bg="black", fg="#03f943", justify="right")

#*************** FILA 1 ***********************************
Button(win, text="7", font=fnt, width=5, height=2, command=lambda:show("7")) .grid(row=1, column=0, sticky=W+E)
Button(win, text="8", font=fnt, width=5, height=2, command=lambda:show("8")) .grid(row=1, column=1, sticky=W+E)
Button(win, text="9", font=fnt, width=5, height=2, command=lambda:show("9")) .grid(row=1, column=2, sticky=W+E)
Button(win, text="/", font=fnt, width=5, height=2, command=lambda:divi())	  .grid(row=1, column=3, sticky=W+E)
Button(win, text="CE", font=fnt, width=5, height=5, command=borrar)   		  .grid(row=1, column=4, rowspan=2, sticky=W+E)

#*************** FILA 2 ***********************************
Button(win, text="4", font=fnt, width=5, height=2, command=lambda:show("4")).grid(row=2, column=0, sticky=W+E)
Button(win, text="5", font=fnt, width=5, height=2, command=lambda:show("5")).grid(row=2, column=1, sticky=W+E)
Button(win, text="6", font=fnt, width=5, height=2, command=lambda:show("6")).grid(row=2, column=2, sticky=W+E)
Button(win, text="*", font=fnt, width=5, height=2, command=lambda:multi())	 .grid(row=2, column=3, sticky=W+E)

#*************** FILA 3 ***********************
Button(win, text="1", font=fnt, width=5, height=2, command=lambda:show("1"))  .grid(row=3, column=0, sticky=W+E)
Button(win, text="2", font=fnt, width=5, height=2, command=lambda:show("2"))  .grid(row=3, column=1, sticky=W+E)
Button(win, text="3", font=fnt, width=5, height=2, command=lambda:show("3"))  .grid(row=3, column=2, sticky=W+E)
Button(win, text="-", font=fnt, width=5, height=2, command=lambda:resta())	   .grid(row=3, column=3, sticky=W+E)
Button(win, text="=", font=fnt, width=5, height=5, command=lambda:resultado()).grid(row=3, column=4, rowspan=2, sticky=W+E)

#*************** FILA 4 ***********************
Button(win, text="0", font=fnt, width=8, height=2, command=lambda:show("0")).grid(row=4, column=0, columnspan= 2, sticky=W+E)
Button(win, text=",", font=fnt, width=5, height=2, command=lambda:show(".")).grid(row=4, column=2, sticky=W+E)
Button(win, text="+", font=fnt, width=5, height=2, command=lambda:suma())	 .grid(row=4, column=3, sticky=W+E)

root.mainloop()