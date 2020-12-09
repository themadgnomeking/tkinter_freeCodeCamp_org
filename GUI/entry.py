from tkinter import *

root = Tk()

e = Entry(root, width=75, borderwidth=5)
e.pack()
e.get()
e.insert(0, "Enter Your Name: ")

def my_click():
    myLabel = Label(root, text=e.get())
    myLabel.pack()

myButton = Button(root, text="Enter Your Name", command=my_click)
myButton.pack()

root.mainloop()