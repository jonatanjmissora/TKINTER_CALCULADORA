from tkinter import *

#================================================================
# Calculadora simple para manejar conceptos de Python y Tkinter
#================================================================

#RESUELTAS
# comienza con un 0 en pantalla
# no ceros a la izquierda
# no doble coma
# numeros negativos de entrada
# arreglada secuencias erroneas de entradas 3+--6=9, o si empiezo con -3=

#SIN RESOLVER
# arreglar problemas de ingreso de caracteres incorrectos
# programar el ingreso del teclado (bind)

# luego del igual, reseteo ingreso
# arreglar operaciones acumulativas apretando =

# estetica GUI
# poner separacione de miles y millones
# poner el simbolo de la operacion en curso
# estetica de codigo

#*************** CONSTANTES y VARIABLES *******************
str_operacion = ""
primer_numero = "0"
segundo_numero = "0"

fnt = ("Arial", 20)

#*************** FUNC CHECK_IMPUT *************************
def output_format(num):
	# no debe pasar los 12 digitos
	num = str(num)[:16]
	num = float(num)
	# si hay cero/s a la derecha del numero
	if abs(num)-int(abs(num))>0:
		return num	
	else:
		return int(num)

#*************** FUNC SHOW ********************************
def show(chr):
	if len(pantalla.get()) < 16:

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
	global primer_numero, str_operacion
	pantalla.set("0")
	primer_numero = "0"
	str_operacion = ""

#*************** OPERACIONES ******************************
def operacion(simbolo):
	global primer_numero, str_operacion
	
	if simbolo == "+" or simbolo == "-" or simbolo == "*" or simbolo == "/":
		
		# si hay numero en pantalla
		if pantalla.get() != "0" and pantalla.get() != "-":
			str_operacion = simbolo
			primer_numero = pantalla.get()
			pantalla.set("0")
		
		# si empieza negativo
		elif simbolo == "-":
		
			# si hay - - se transforma en un +0
			if pantalla.get() == "-":
				pantalla.set("0")
			else:
				pantalla.set("-")
	
	elif simbolo == "=":
		if pantalla.get() != "-":
			if str_operacion == "+":
				resultado = float(primer_numero) + float(pantalla.get())
				pantalla.set(output_format(resultado))
			elif str_operacion == "-":
				resultado = float(primer_numero) - float(pantalla.get())
				pantalla.set(output_format(resultado))
			elif str_operacion == "*":
				resultado = float(primer_numero) * float(pantalla.get())
				pantalla.set(output_format(resultado)) 
			elif str_operacion == "/":
				# no a la division por 0
				if pantalla.get() != "0":
					resultado = float(primer_numero) / float(pantalla.get())
					pantalla.set(output_format(resultado))
	
root = Tk()
root.title("CALCULADORA")
root.resizable(False, False)
win = Frame(root)
win.grid(row=0, column=0, padx=10, pady=10)

#*************** PANTALLA *********************************
pantalla = StringVar()
pantalla.set("0")
visor = Entry(win, textvariable=pantalla, width=16, font=("Arial", 31))
visor.grid(row=0, column=0, pady=10, columnspan=5)
visor.config(bg="black", fg="#03f943", justify="right")

#*************** FILA 1 ***********************************
Button(win, text="7", font=fnt, width=3, height=2, command=lambda:show("7")) 	 .grid(row=1, column=0, sticky=W+E)
Button(win, text="8", font=fnt, width=3, height=2, command=lambda:show("8")) 	 .grid(row=1, column=1, sticky=W+E)
Button(win, text="9", font=fnt, width=3, height=2, command=lambda:show("9")) 	 .grid(row=1, column=2, sticky=W+E)
Button(win, text="/", font=fnt, width=3, height=2, command=lambda:operacion("/")).grid(row=1, column=3, sticky=W+E)
Button(win, text="CE", font=fnt, width=3, height=2, command=borrar)   		  	 .grid(row=1, column=4, rowspan=2, sticky=W+E+N+S)

#*************** FILA 2 ***********************************
Button(win, text="4", font=fnt, width=3, height=2, command=lambda:show("4"))	 .grid(row=2, column=0, sticky=W+E)
Button(win, text="5", font=fnt, width=3, height=2, command=lambda:show("5"))	 .grid(row=2, column=1, sticky=W+E)
Button(win, text="6", font=fnt, width=3, height=2, command=lambda:show("6"))	 .grid(row=2, column=2, sticky=W+E)
Button(win, text="*", font=fnt, width=3, height=2, command=lambda:operacion("*")).grid(row=2, column=3, sticky=W+E)

#*************** FILA 3 ***********************
Button(win, text="1", font=fnt, width=3, height=2, command=lambda:show("1"))  	 .grid(row=3, column=0, sticky=W+E)
Button(win, text="2", font=fnt, width=3, height=2, command=lambda:show("2"))  	 .grid(row=3, column=1, sticky=W+E)
Button(win, text="3", font=fnt, width=3, height=2, command=lambda:show("3"))  	 .grid(row=3, column=2, sticky=W+E)
Button(win, text="-", font=fnt, width=3, height=2, command=lambda:operacion("-")).grid(row=3, column=3, sticky=W+E)
Button(win, text="=", font=fnt, width=3, height=2, command=lambda:operacion("=")).grid(row=3, column=4, rowspan=2, sticky=W+E+N+S)

#*************** FILA 4 ***********************
Button(win, text="0", font=fnt, width=3, height=2, command=lambda:show("0"))	 .grid(row=4, column=0, columnspan= 2, sticky=W+E)
Button(win, text=",", font=fnt, width=3, height=2, command=lambda:show("."))	 .grid(row=4, column=2, sticky=W+E)
Button(win, text="+", font=fnt, width=3, height=2, command=lambda:operacion("+")).grid(row=4, column=3, sticky=W+E)

root.mainloop()