from tkinter import *

root = Tk()

def my_click():
    myLabel = Label(root, text="You clicked the button")
    myLabel.pack()

my_button = Button(root, text="Click MEH!!!!!", padx=50, pady=30, command=my_click)
my_button.pack()

root.mainloop()