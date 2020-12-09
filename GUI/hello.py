from tkinter import *

root = Tk()

myLabel1 = Label(root, text="Hello World!")
myLable2 = Label(root, text="My name is Tims Guynes")

myLabel1.grid(row=0, column=0)
myLable2.grid(row=1, column=1)

root.mainloop()