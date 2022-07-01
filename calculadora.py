from tkinter import*
import tkinter as tk
from math import*
#crear ventana
ventana = Tk()
ventana.title("calculadora cientifica")
ventana.geometry('450x500')
ventana.configure(background='seashell')
#variables
def bclick(num):
    global operador
    operador = operador + str(num)
    a.set(operador)
def clear():
    global operador
    operador = ("")
    a.set("0")
def operacion():
    global operador
    try:
        opera = str(eval(operador))
        a.set(opera)
    except:
        a.set("ERROR")
    operador=""
a = StringVar()
operador = ""
#ventanita
display = Entry(ventana, font=("arial",20,"bold"), bg ='#747f91',bd=15,insertwidth=4,justify="right", textvariable= a )
display.pack(fill=tk.X, ipadx=10, ipady=10)
#botones primera linea
raiz=Button(ventana,text="√", width=11, height=3, command=lambda:bclick("sqrt"))
raiz.place(x=1, y=85)
exponente=Button(ventana,text="EXP", width=11, height=3, command=lambda:bclick("**"))
exponente.place(x=90, y=85)
logaritmo=Button(ventana,text="LOG", width=11, height=3, command=lambda:bclick("log10"))
logaritmo.place(x=179, y=85)
ln=Button(ventana,text="LN", width=11, height=3, command=lambda:bclick("log"))
ln.place(x=268, y=85)
pi=Button(ventana,text="π",width=11, height=3, command=lambda:bclick("3,1415926535897932"))
pi.place(x=357, y=85)
#botones segunda linea
porcentaje=Button(ventana,text="%", width=11, height=3, command=lambda:bclick("%"))
porcentaje.place(x=1, y=143)
multiplicacion=Button(ventana,text="x", width=11, height=3, command=lambda:bclick("*"))
multiplicacion.place(x=90, y=143)
division= Button(ventana,text="÷", width=11, height=3, command=lambda:bclick("/"))
division.place(x=179, y=143)
parentesisd=Button(ventana,text="(", width=11, height=3, command=lambda:bclick("("))
parentesisd.place(x=268, y=143)
parentesisI= Button(ventana,text=")", width=11, height=3, command=lambda:bclick(")"))
parentesisI.place(x=357, y=143)
#botones tercera fila, numeros
numero7=Button(ventana,text="7", width=11, height=3, command=lambda:bclick(7))
numero7.place(x=1, y=201)
numero8=Button(ventana,text="8", width=11, height=3, command=lambda:bclick(8))
numero8.place(x=90, y=201)
numero9=Button(ventana,text="9", width=11, height=3, command=lambda:bclick(9))
numero9.place(x=179, y=201)
AC=Button(ventana,text="AC", width=24, height=3, command=lambda: clear())
AC.place(x=268, y=201)
#botones cuarta fila,numeros
numero4=Button(ventana,text="4", width=11, height=3, command=lambda:bclick(4))
numero4.place(x=1, y=259)
numero5=Button(ventana,text="5", width=11, height=3, command=lambda:bclick(5))
numero5.place(x=90, y=259)
numero6=Button(ventana,text="6", width=11, height=3, command=lambda:bclick(6))
numero6.place(x=179, y=259)
multiplicacion=Button(ventana,text="x", width=11, height=3, command=lambda:bclick("*"))
multiplicacion.place(x=268, y=259)
division= Button(ventana,text="÷", width=11, height=3, command=lambda:bclick("/"))
division.place(x=357, y=259)
#quinta fila, numeros
numero1=Button(ventana,text="1", width=11, height=3, command=lambda:bclick(1))
numero1.place(x=1, y=317)
numero2=Button(ventana,text="2", width=11, height=3, command=lambda:bclick(2))
numero2.place(x=90, y=317)
numero3=Button(ventana,text="3", width=11, height=3, command=lambda:bclick(3))
numero3.place(x=179, y=317)
suma=Button(ventana,text="+", width=11, height=3, command=lambda:bclick("+"))
suma.place(x=268, y=317)
resta=Button(ventana,text="-", width=11, height=3, command=lambda:bclick("-"))
resta.place(x=357, y=317)
#sexta fila
coma=Button(ventana,text=",", width=11, height=3, command=lambda:bclick(","))
coma.place(x=1, y=375)
numero0 = Button(ventana,text="0", width=11, height=3, command=lambda:bclick(0))
numero0.place(x=90, y=375)
igual= Button(ventana,text="=", width=37, height=3, command=lambda:operacion())
igual.place(x=179, y=375)


#otros(salen aprox no exacto, no se cuenta)
coseno=Button(ventana,text="cos", width=11, height=3, command=lambda:bclick("cos"))
coseno.place(x=1, y=433)
seno =Button(ventana,text="sin", width=11, height=3, command=lambda:bclick("sin"))
seno.place(x=90, y=433)
tangente = Button(ventana,text="tan", width=11, height=3, command=lambda:bclick("tan"))
tangente.place(x=179, y=433)
ventana.mainloop()
