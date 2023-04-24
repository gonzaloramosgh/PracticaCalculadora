import tkinter
from tkinter import *

raiz = Tk()
raiz.config(bg="black")
raiz.title("CALCULADORA")


i=0

#Fila 0 DISPLAY O ENTRADA

Resultado = Entry (raiz, bg='silver', width=19, relief='groove', font='Montserrat 16',borderwidth=2,justify='right')
Resultado.grid (columnspan=4, row=0,padx=5 ,pady=5 )

def Apretar_Boton(valor):
	global i
	Resultado.insert (i, valor)
	i += 1

def BorrarTodo():
	global i
	Resultado.delete(i,END)
	i = 0
	return Resultado.delete(i,END)


def BorrarUno():
	global i
	Resultado.delete(i)
	i -= 1


def Imprimir_resultado():
	cuenta = Resultado.get()
	BorrarTodo()
	Resultado.insert(0,eval(cuenta))
	i=0
ventana = Frame(raiz,width=500,height=500)


def Apagando():
	sys.exit()

#BOTONES

boton1=Button(raiz,text=1,width=5,height=2,command=lambda :Apretar_Boton(1))
boton2=Button(raiz,text="2",width=5,height=2,command=lambda :Apretar_Boton(2))
boton3=Button(raiz,text="3",width=5,height=2,command=lambda :Apretar_Boton(3))
boton4=Button(raiz,text="4",width=5,height=2,command=lambda :Apretar_Boton(4))
boton5=Button(raiz,text="5",width=5,height=2,command=lambda :Apretar_Boton(5))
boton6=Button(raiz,text="6",width=5,height=2,command=lambda :Apretar_Boton(6))
boton7=Button(raiz,text="7",width=5,height=2,command=lambda :Apretar_Boton(7))
boton8=Button(raiz,text="8",width=5,height=2,command=lambda :Apretar_Boton(8))
boton9=Button(raiz,text="9",width=5,height=2,command=lambda :Apretar_Boton(9))
boton0=Button(raiz,text="0",width=5,height=2,command=lambda :Apretar_Boton(0))

botonSuma=Button(raiz,text="+",width=5,height=6,command=lambda :Apretar_Boton("+"))
botonResta=Button(raiz,text="-",width=5,height=2,command=lambda :Apretar_Boton("-"))
botonMulti=Button(raiz,text="*",width=5,height=2,command=lambda :Apretar_Boton("*"))
botonDiv=Button(raiz,text="/",width=5,height=2,command=lambda :Apretar_Boton("/"))

botonRaiz=Button(raiz,text="⌫",width=5,height=2,command=lambda : BorrarUno())

botonIgual=Button(raiz,text="=",width=5,height=2,command=Imprimir_resultado)
botonBorrarUno=Button(raiz,text="OFF",width=5,height=2,command=Apagando)
botonBorrarTodo=Button(raiz,text="C",width=5,height=2,command=BorrarTodo)
botonPunto=Button(raiz,text=".",width=5,height=2,command=lambda :Apretar_Boton("."))

#AGREGAR BOTONES EN PANTALLA LOS UBICA

botonBorrarUno.grid(row=1,column=0,padx = 5,pady=5)
botonBorrarTodo.grid(row=1,column=1,padx = 5,pady=5)
botonRaiz.grid(row=1,column=2,padx = 5,pady=5)
botonDiv.grid(row=1,column=3,padx=5,pady=5)

boton7.grid(row=2,column=0,padx = 5,pady=5)
boton8.grid(row=2,column=1,padx = 5,pady=5)
boton9.grid(row=2,column=2,padx = 5,pady=5)
boton4.grid(row=3,column=0,padx = 5,pady=5)
boton5.grid(row=3,column=1,padx = 5,pady=5)
boton6.grid(row=3,column=2,padx = 5,pady=5)
boton1.grid(row=4,column=0,padx = 5,pady=5)
boton2.grid(row=4,column=1,padx = 5,pady=5)
boton3.grid(row=4,column=2,padx = 5,pady=5)
botonPunto.grid(row=5,column=0,padx = 5,pady=5)
boton0.grid(row=5,column=1,padx = 5,pady=5)
botonIgual.grid(row=5,column=2,padx = 5,pady=5)
botonSuma.grid(row=4,column=3,rowspan=2,padx=5,pady=5)
botonMulti.grid(row=2,column=3,padx=5,pady=5)
botonResta.grid(row=3,column=3,padx=5,pady=5)

raiz.mainloop()