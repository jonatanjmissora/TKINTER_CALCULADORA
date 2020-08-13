from tkinter import *

#================================================================
# Calculadora simple para manejar conceptos de Python y Tkinter
#================================================================

#RESUELTAS
# comienza con un 0 en pantalla
# no ceros a la izquierda
# no doble coma

#SIN RESOLVER
# arreglar problemas de ingreso de caracteres incorrectos
# arreglar secuencias erroneas de entrada, si empiezo con operacion antes de numero, o si presiono 2 operaciones seguidas
# programar el ingreso del teclado (bind)

# luego del igual, reseteo ingreso
# arreglar operaciones acumulativas apretando =
# arreglar operaciones con float
# ver que pasa con numero negativos

# estetica GUI
# poner separacione de miles y millones
# poner el simbolo de la operacion en curso
# estetica de codigo

#*************** CONSTANTES y VARIABLES *******************
operacion=""
primer_numero="0"

fnt = ("Arial", 15)
"""
#*************** FUNC FLOAT_CHECK *************************
def check_imput(chr):
	pass

#*************** FUNC FLOAT_CHECK *************************
def float_check(num):
	if num-int(num)>0:
		return num
	else:
		return int(num)
"""
#*************** FUNC SHOW ********************************
def show(chr):
	global operacion
	# no permitimos ceros a la izquierda
	if chr == "0":		
		if pantalla.get() != "0":
			pantalla.set(pantalla.get() + chr)
	# no permitimos doble coma
	elif chr == ".":
		if "." not in pantalla.get():
			pantalla.set(pantalla.get() + chr)
	# si esta en cero la pantalla, comenzamos con el primer chr
	elif pantalla.get() == "0":
		pantalla.set(chr)
	# si ya hay numero, concateno
	else: 
		pantalla.set(pantalla.get() + chr)

#*************** BORRAR PANTALLA **************************
def borrar():
	global primer_numero
	pantalla.set("0")
	primer_numero = "0"

#*************** OPERACIONES ******************************
def operacion(simbol):
	global primer_numero	
	if simbol == "+":
		primer_numero = pantalla.get()
		pantalla.set("0")
	if simbol == "=":
		segundo_numero = pantalla.get()
		pantalla.set(int(segundo_numero) + int(primer_numero))


root=Tk()
root.title("CALCULADORA")
root.resizable(False, False)
win = Frame(root)
win.grid(row=0, column=0, padx=10, pady=10)

#*************** PANTALLA *********************************
pantalla=StringVar()
pantalla.set("0")
visor=Entry(win, textvariable=pantalla, width=12, font=("Arial", 35))
visor.grid(row=0, column=0, pady=10, columnspan=5)
visor.config(bg="black", fg="#03f943", justify="right")

#*************** FILA 1 ***********************************
Button(win, text="7", font=fnt, width=5, height=2, command=lambda:show("7")) .grid(row=1, column=0, sticky=W+E)
Button(win, text="8", font=fnt, width=5, height=2, command=lambda:show("8")) .grid(row=1, column=1, sticky=W+E)
Button(win, text="9", font=fnt, width=5, height=2, command=lambda:show("9")) .grid(row=1, column=2, sticky=W+E)
Button(win, text="/", font=fnt, width=5, height=2, command=lambda:operacion("/"))	  .grid(row=1, column=3, sticky=W+E)
Button(win, text="CE", font=fnt, width=5, height=5, command=borrar)   		  .grid(row=1, column=4, rowspan=2, sticky=W+E)

#*************** FILA 2 ***********************************
Button(win, text="4", font=fnt, width=5, height=2, command=lambda:show("4")).grid(row=2, column=0, sticky=W+E)
Button(win, text="5", font=fnt, width=5, height=2, command=lambda:show("5")).grid(row=2, column=1, sticky=W+E)
Button(win, text="6", font=fnt, width=5, height=2, command=lambda:show("6")).grid(row=2, column=2, sticky=W+E)
Button(win, text="*", font=fnt, width=5, height=2, command=lambda:operacion("*"))	 .grid(row=2, column=3, sticky=W+E)

#*************** FILA 3 ***********************
Button(win, text="1", font=fnt, width=5, height=2, command=lambda:show("1"))  .grid(row=3, column=0, sticky=W+E)
Button(win, text="2", font=fnt, width=5, height=2, command=lambda:show("2"))  .grid(row=3, column=1, sticky=W+E)
Button(win, text="3", font=fnt, width=5, height=2, command=lambda:show("3"))  .grid(row=3, column=2, sticky=W+E)
Button(win, text="-", font=fnt, width=5, height=2, command=lambda:operacion("-"))	   .grid(row=3, column=3, sticky=W+E)
Button(win, text="=", font=fnt, width=5, height=5, command=lambda:operacion("=")).grid(row=3, column=4, rowspan=2, sticky=W+E)

#*************** FILA 4 ***********************
Button(win, text="0", font=fnt, width=8, height=2, command=lambda:show("0")).grid(row=4, column=0, columnspan= 2, sticky=W+E)
Button(win, text=",", font=fnt, width=5, height=2, command=lambda:show(".")).grid(row=4, column=2, sticky=W+E)
Button(win, text="+", font=fnt, width=5, height=2, command=lambda:operacion("+"))	 .grid(row=4, column=3, sticky=W+E)

root.mainloop()