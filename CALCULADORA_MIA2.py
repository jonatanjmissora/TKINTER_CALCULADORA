from tkinter import *

root=Tk()
root.title("CALCULADORA")
operacion=""
igual=False
resultado=0

#*************** PANTALLA *********************** 
numero=StringVar()
pantalla = Entry(root, textvariable=numero, justify="right")
pantalla.grid(row=1, column=1, columnspan=4, pady=10)	#columnspan le digo que ocupe 4 columnas

#*************** FUNC FLOAT_CHECK *********************** 
def float_check(num):
	if num-int(num)>0:
		return num
	else:
		return int(num)

#*************** FUNC SHOW *********************** 
def show(num):
	global operacion
	global igual
	if operacion=="":
		if not igual:
			numero.set(numero.get() + num)
		else:
			igual=False
			numero.set(num)
			operacion=""
	else:
		numero.set(num)
		operacion=""

#*************** BORRAR PANTALLA *********************** 
def borrar():
	numero.set("")


#*************** FUNC SUMA *********************** 	
def suma(num):
	global operacion
	global resultado
	resultado += float_check(float(num))
	operacion = "suma"
	numero.set(resultado)

#*************** FUNC RESTA *********************** 	
def resta(num):
	global operacion
	global resultado
	resultado = float_check(float(num))
	operacion = "resta"
	numero.set(resultado)

#*************** FUNC EL_RESULTADO ***********************
def el_resultado():
	global operacion
	global resultado
	global igual
	igual=True
	if operacion=="suma":
		numero.set(float_check(resultado + float(numero.get())))
		operacion=""
	elif operacion=="resta":
		numero.set(float_check(resultado - float(numero.get())))
		operacion=""
	resultado=0


#*************** FILA 1 ***********************
Button(root, text="7", command=lambda:show("7")).grid(row=2, column=1, sticky=W+E)
Button(root, text="8", command=lambda:show("8")).grid(row=2, column=2, sticky=W+E)
Button(root, text="9", command=lambda:show("9")).grid(row=2, column=3, sticky=W+E)
Button(root, text="/").grid(row=2, column=4, sticky=W+E)

#*************** FILA 2 ***********************
Button(root, text="4", command=lambda:show("4")).grid(row=3, column=1, sticky=W+E)
Button(root, text="5", command=lambda:show("5")).grid(row=3, column=2, sticky=W+E)
Button(root, text="6", command=lambda:show("6")).grid(row=3, column=3, sticky=W+E)
Button(root, text="*").grid(row=3, column=4, sticky=W+E)

#*************** FILA 3 ***********************
Button(root, text="1", command=lambda:show("1")).grid(row=4, column=1, sticky=W+E)
Button(root, text="2", command=lambda:show("2")).grid(row=4, column=2, sticky=W+E)
Button(root, text="3", command=lambda:show("3")).grid(row=4, column=3, sticky=W+E)
Button(root, text="-", command=lambda:resta(numero.get())).grid(row=4, column=4, sticky=W+E)

#*************** FILA 4 ***********************
Button(root, text="0", command=lambda:borrar()).grid(row=5, column=1, sticky=W+E)
Button(root, text=",", command=lambda:show(".")).grid(row=5, column=2, sticky=W+E)
Button(root, text="=", command=lambda:el_resultado()).grid(row=5, column=3, sticky=W+E)
Button(root, text="+", command=lambda:suma(numero.get())).grid(row=5, column=4, sticky=W+E)

root.mainloop()