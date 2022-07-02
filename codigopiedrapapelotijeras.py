import tkinter
from tkinter import *
import random
ventana = Tk()
ventana.geometry("500x500")
ventana.title("piedra papel o tijeras")
computer_value = {
    "0": "piedra",
    "1": "papel",
    "2": "tijeras" }
def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text="jugador")
    l3.config(text="computador")
    l4.config(text="")
def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"
def piedra():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "piedra":
        match_result = "empate"
    elif c_v == "tijeras":
        match_result = "jugador gana"
    else:
        match_result = "computador gana"
    l4.config(text=match_result)
    l1.config(text="piedra")
    l3.config(text=c_v)
    button_disable()
def papel():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "papel":
        match_result = "empate"
    elif c_v == "tijeras":
        match_result = "computador gana"
    else:
        match_result = "jugador gana"
    l4.config(text=match_result)
    l1.config(text="papel")
    l3.config(text=c_v)
    button_disable()
def tijeras():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "piedra":
        match_result = "computador gana"
    elif c_v == "tijeras":
        match_result = "empate"
    else:
        match_result = "jugador gana"
    l4.config(text=match_result)
    l1.config(text="tijeras")
    l3.config(text=c_v)
    button_disable()
Label(ventana,
      text="piedra papel tijeras",
      font="normal 20 bold",
      fg="blue").pack(pady=20)
frame = Frame(ventana)
frame.pack()
l1 = Label(frame,
           text="jugador",
           font=10)
l2 = Label(frame,
           text=" VS ",
           font="normal 10 bold")
l3 = Label(frame, text="computadora", font=10)
l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()
l4 = Label(ventana,
           text="",
           font="normal 20 bold",
           bg="white",
           width=15,
           borderwidth=2,
           relief="solid")
l4.pack(pady=20)
frame1 = Frame(ventana)
frame1.pack()
b1 = Button(frame1, text="piedra",
            font=10, width=7,
            command=piedra)
b2 = Button(frame1, text="papel",
            font=10, width=7,
            command=papel)
b3 = Button(frame1, text="tijeras",
            font=10, width=7,
            command=tijeras)
b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)
Button(ventana, text="Reset Game",
       font=10, fg="red",
       bg="black", command=reset_game).pack(pady=20)
ventana.mainloop()
