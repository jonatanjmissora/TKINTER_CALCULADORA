from tkinter import *

root=Tk()
miFrame=Frame(root, width=500, height=400)
miFrame.pack()
operacion=""
resultado=0

#*************** PANTALLA *********************** 
numero=StringVar()
pantalla=Entry(miFrame, textvariable=numero, width=20, font=("Arial", 15))
pantalla.grid(row=1, column=1, padx=5, pady=5, columnspan=5)	#columnspan le digo que ocupe 4 columnas
pantalla.config(bg="black", fg="#03f943", justify="right")

def show(num):
	global operacion
	if operacion!="":
		numero.set(num)
		operacion=""
	else:
		numero.set(numero.get() + num)

#*************** FUNC FLOAT_CHECK *********************** 
def float_check(num):
	if num-int(num)>0:
		return num
	else:
		return int(num)

#*************** FUNC SUMA *********************** 	
def suma(num):
	global operacion
	global resultado
	resultado += float(num)
	operacion = "suma"
	numero.set(resultado)

#*************** FUNC EL_RESULTADO ***********************
def el_resultado():
	global resultado
	numero.set(resultado+float(numero.get()))
	resultado=0

#*************** FILA 1 ***********************
B7=Button(miFrame, 		  text="7", width=3, command=lambda:show("7")) 	# width es ancho de boton
B8=Button(miFrame, 		  text="8", width=3, command=lambda:show("8"))
B9=Button(miFrame, 		  text="9", width=3, command=lambda:show("9"))
BDivision=Button(miFrame, text="/", width=3)
BBorrar=Button(miFrame,   text="CE", width=3, height=3)

B7.grid(	   row=2, column=1)
B8.grid(	   row=2, column=2)
B9.grid(	   row=2, column=3)
BDivision.grid(row=2, column=4)
BBorrar.grid(  row=2, column=5, rowspan=2)

#*************** FILA 2 ***********************
B4=Button(			   miFrame, text="4", width=3, command=lambda:show("4")) 	# width es ancho de boton
B5=Button(			   miFrame, text="5", width=3, command=lambda:show("5"))
B6=Button(			   miFrame, text="6", width=3, command=lambda:show("6"))
BMultiplicacion=Button(miFrame, text="*", width=3)

B4.grid(			 row=3, column=1)
B5.grid(		     row=3, column=2)
B6.grid(			 row=3, column=3)
BMultiplicacion.grid(row=3, column=4)

#*************** FILA 3 ***********************
B1=Button(		  miFrame, text="1", width=3, command=lambda:show("1")) 	# width es ancho de boton
B2=Button(		  miFrame, text="2", width=3, command=lambda:show("2"))
B3=Button(		  miFrame, text="3", width=3, command=lambda:show("3"))
BResta=Button(	  miFrame, text="-", width=3)
BResultado=Button(miFrame, text="=", width=3, height=3)

B1.grid(		row=4, column=1)
B2.grid(		row=4, column=2)
B3.grid(		row=4, column=3)
BResta.grid(	row=4, column=4)
BResultado.grid(row=4, column=5, rowspan=2)

#*************** FILA 4 ***********************
B0=Button(    miFrame, text="0", width=10, command=lambda:show("0")) 	# width es ancho de boton
BComa=Button( miFrame, text=",", width=3, command=lambda:show("."))
BIgual=Button(miFrame, text="=", width=3, command=lambda:el_resultado())
BSuma=Button( miFrame, text="+", width=3, command=lambda:suma(numero.get()))

B0.grid(   row=5, column=1, columnspan=2)
BComa.grid(row=5, column=3)
BSuma.grid(row=5, column=4)

root.mainloop()