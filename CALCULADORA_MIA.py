from tkinter import *

root=Tk()
miFrame=Frame(root, width=500, height=400)
miFrame.pack()
operacion=""
resultado=0

#*************** PANTALLA *********************** 
numero=StringVar()
pantalla=Entry(miFrame, textvariable=numero)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)	#columnspan le digo que ocupe 4 columnas
pantalla.config(bg="black", fg="#03f943", justify="right")

def show(num):
	global operacion
	if operacion!="":
		numero.set(num)
		operacion=""
	else:
		numero.set(numero.get() + num)

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
B7=Button(miFrame, text="7", width=3, command=lambda:show("7")) 	# width es ancho de boton
B7.grid(row=2, column=1)
B8=Button(miFrame, text="8", width=3, command=lambda:show("8"))
B8.grid(row=2, column=2)
B9=Button(miFrame, text="9", width=3, command=lambda:show("9"))
B9.grid(row=2, column=3)
BDiv=Button(miFrame, text="/", width=3)
BDiv.grid(row=2, column=4)

#*************** FILA 2 ***********************
B4=Button(miFrame, text="4", width=3, command=lambda:show("4")) 	# width es ancho de boton
B4.grid(row=3, column=1)
B5=Button(miFrame, text="5", width=3, command=lambda:show("5"))
B5.grid(row=3, column=2)
B6=Button(miFrame, text="6", width=3, command=lambda:show("6"))
B6.grid(row=3, column=3)
BMult=Button(miFrame, text="*", width=3)
BMult.grid(row=3, column=4)

#*************** FILA 3 ***********************
B1=Button(miFrame, text="1", width=3, command=lambda:show("1")) 	# width es ancho de boton
B1.grid(row=4, column=1)
B2=Button(miFrame, text="2", width=3, command=lambda:show("2"))
B2.grid(row=4, column=2)
B3=Button(miFrame, text="3", width=3, command=lambda:show("3"))
B3.grid(row=4, column=3)
BRest=Button(miFrame, text="-", width=3)
BRest.grid(row=4, column=4)

#*************** FILA 4 ***********************
B0=Button(miFrame, text="0", width=3, command=lambda:show("0")) 	# width es ancho de boton
B0.grid(row=5, column=1)
BComa=Button(miFrame, text=",", width=3, command=lambda:show("."))
BComa.grid(row=5, column=2)
BIgu=Button(miFrame, text="=", width=3, command=lambda:el_resultado())
BIgu.grid(row=5, column=3)
BSum=Button(miFrame, text="+", width=3, command=lambda:suma(numero.get()))
BSum.grid(row=5, column=4)

root.mainloop()