from tkinter import *

myCal = Tk()

def equal():
    secondNum = int(inputfield.get())
    inputfield.delete(0, END)
    if formula == "add":
        inputfield.insert(0, temp + secondNum)
    elif formula == "sub":
        inputfield.insert(0, temp - secondNum)
    elif formula == "mul":
        inputfield.insert(0, temp * secondNum)
    elif formula == "div":
        inputfield.insert(0, temp / secondNum)

def calc(math):
    number = int(inputfield.get())
    global temp
    global formula
    temp = number
    formula = math
    inputfield.delete(0, END)

def addnum(num):
    inputfield.insert(END, num)
    
def clear():
    inputfield.delete(0, END)

myCal.title("Basic Calculator")
inputfield = Entry(width=45)
inputfield.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

rowCount = 4
colCount = 0

for i in range(10):
    numButton = Button(text=str(i), padx=40, pady=20, command=lambda i=i: addnum(i)).grid(row=rowCount, column=colCount)
    colCount += 1
    if i % 3 == 0:
        rowCount -= 1
        colCount = 0

clearButton = Button(text="Clear", padx=86, pady=20, command=clear).grid(row=4, column=1, columnspan=2)
plusButton = Button(text="+", padx=39, pady=20, command=lambda: calc("add")).grid(row=5, column=0)
equalButton = Button(text="=", padx=96, pady=20, command=equal).grid(row=5, column=1, columnspan=2)
minusButton = Button(text="-", padx=41, pady=20, command=lambda: calc("sub")).grid(row=6, column=0)
multiButton = Button(text="*", padx=41, pady=20, command=lambda: calc("mul")).grid(row=6, column=1)
divideButton = Button(text="/", padx=41, pady=20, command=lambda: calc("div")).grid(row=6, column=2)

myCal.mainloop()