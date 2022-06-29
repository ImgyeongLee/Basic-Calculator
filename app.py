from tkinter import *

myCal = Tk()

myCal.title("Basic Calculator")
inputfield = Entry(width=45)
inputfield.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

rowCount = 4
colCount = 0

for i in range(10):
    numButton = Button(text=str(i), padx=40, pady=20).grid(row=rowCount, column=colCount)
    colCount += 1
    if i % 3 == 0:
        rowCount -= 1
        colCount = 0

clearButton = Button(text="Clear", padx=80, pady=20).grid(row=4, column=1, columnspan=2)
plusButton = Button(text="+", padx=40, pady=20).grid(row=5, column=0)
equalButton = Button(text="=", padx=80, pady=20).grid(row=5, column=1, columnspan=2)

myCal.mainloop()