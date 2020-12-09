from tkinter import *

root = Tk()
root.title("Python Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0,str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    firstNumber = e.get()
    global fstNum
    global math
    math = "addition"
    fstNum = int(firstNumber)
    e.delete(0, END)

def button_subtract():
    firstNumber = e.get()
    global fstNum
    global math
    math = "subtraction"
    fstNum = int(firstNumber)
    e.delete(0, END)

def button_multiply():
    firstNumber = e.get()
    global fstNum
    global math
    math = "multiplication"
    fstNum = int(firstNumber)
    e.delete(0, END)

def button_divide():
    firstNumber = e.get()
    global fstNum
    global math
    math = "division"
    fstNum = int(firstNumber)
    e.delete(0, END)

def button_equal():
    secondNumber = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, fstNum + int(secondNumber))
    
    if math == "subtraction":
        e.insert(0, fstNum - int(secondNumber))

    if math == "multiplication":
        e.insert(0, fstNum * int(secondNumber))

    if math == "division":
        e.insert(0, fstNum / int(secondNumber))
    


#devine the buttons needed
buttonWidth = 40
buttonLenth = 20

button01 = Button(root, text="1", padx=buttonWidth, pady=buttonLenth, command=lambda: button_click(1))
button02 = Button(root, text="2", padx=buttonWidth, pady=buttonLenth, command=lambda: button_click(2))
button03 = Button(root, text="3", padx=buttonWidth, pady=buttonLenth, command=lambda: button_click(3))
button04 = Button(root, text="4", padx=buttonWidth, pady=buttonLenth, command=lambda: button_click(4))
button05 = Button(root, text="5", padx=buttonWidth, pady=buttonLenth, command=lambda: button_click(5))
button06 = Button(root, text="6", padx=buttonWidth, pady=buttonLenth, command=lambda: button_click(6))
button07 = Button(root, text="7", padx=buttonWidth, pady=buttonLenth, command=lambda: button_click(7))
button08 = Button(root, text="8", padx=buttonWidth, pady=buttonLenth, command=lambda: button_click(8))
button09 = Button(root, text="9", padx=buttonWidth, pady=buttonLenth, command=lambda: button_click(9))
button00 = Button(root, text="0", padx=buttonWidth, pady=buttonLenth, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_subtract = Button(root, text="-", padx=39, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=39, pady=20, command=button_multiply)
button_divide= Button(root, text="/", padx=39, pady=20, command=button_divide)

button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)


#get the buttons on the screen
button01.grid(row=3 ,column=2)
button02.grid(row=3 ,column=1)
button03.grid(row=3 ,column=0)

button04.grid(row=2 ,column=2)
button05.grid(row=2 ,column=1)
button06.grid(row=2 ,column=0)

button07.grid(row=1 ,column=2)
button08.grid(row=1 ,column=1)
button09.grid(row=1 ,column=0)

button00.grid(row=4 ,column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

button_equal.grid(row=5, column=0,columnspan=4)


root.mainloop()