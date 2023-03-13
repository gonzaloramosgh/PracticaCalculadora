import tkinter
from tkinter import *

raiz = Tk()
ventana = Frame(raiz,width=500,height=500)

botonzzz=Button(raiz, text="DISPLAY",padx=25,pady=25).grid(row=0,column=1)
boton7=Button(raiz, text="7",padx=25,pady=25).grid(row=1,column=0)
boton8=Button(raiz, text="8",padx=25,pady=25).grid(row=1,column=1)
boton9=Button(raiz, text="9",padx=25,pady=25).grid(row=1,column=2)

boton4=Button(raiz, text="4",padx=25,pady=25).grid(row=2,column=0)
boton5=Button(raiz, text="5",padx=25,pady=25).grid(row=2,column=1)
boton6=Button(raiz, text="6",padx=25,pady=25).grid(row=2,column=2)

boton1=Button(raiz, text="1",padx=25,pady=25).grid(row=3,column=0)
boton2=Button(raiz, text="2",padx=25,pady=25).grid(row=3,column=1)
boton3=Button(raiz, text="3",padx=25,pady=25).grid(row=3,column=2)

botonC=Button(raiz, text="C",padx=25,pady=25).grid(row=4,column=0)
boton0=Button(raiz, text="0",padx=25,pady=25).grid(row=4,column=1)
botonPunto=Button(raiz, text=".",padx=25,pady=25).grid(row=4,column=2)

botonMas=Button(raiz, text="+",padx=25,pady=25).grid(row=1,column=4)
botonMenos=Button(raiz, text="-",padx=25,pady=25).grid(row=2,column=4)
botonDivision=Button(raiz, text="%",padx=25,pady=25).grid(row=3,column=4)
botonMultiplicacion = Button(raiz,text="x",padx=25,pady=25).grid(row=4,column=4)
botonIgual=Button(raiz, text="=",padx=25).grid(row=5)


raiz.mainloop()