from tkinter import *

root = Tk()

"""
# Variables dinamicas
texto = StringVar()
texto.set("Un nuevo texto")

label = Label(root, text= "Hola mundo")
label.pack(anchor="nw")
Label(root, text= "Otra etiqueta").pack(anchor="center")
Label(root, text= "Hola Marte").pack(anchor="se")

label.config(bg="green", fg="blue", font=("Verdena", 24))
label.config(textvariable=texto)"""


imagen = PhotoImage(file="rz.png")
Label(root, image=imagen, bd=0).pack(side= "left")

root.mainloop() 
