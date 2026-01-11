from tkinter import *

window = Tk()

window.title("Calculator")

input_data = Entry(window, width=55, borderwidth=2)
input_data.grid(row=0, column=0,pady=20,columnspan=4)

def button_click(number:str) -> None:
    input_data.insert(END, number)

def addition() -> None:
    input_data.insert(END, " + ")

def subtraction() -> None:
    input_data.insert(END, " - ")

def clear() -> None:
    input_data.delete(0, END)

def equal_to() -> None:
    expression = input_data.get()
    result = eval(expression)
    input_data.delete(0, END)
    input_data.insert(0, result)


button_1 = Button(window, text="1", padx=40, pady=30,command=lambda: button_click('1'))
button_2 = Button(window, text="2", padx=40, pady=30,command=lambda: button_click('2'))
button_3 = Button(window, text="3", padx=40, pady=30,command=lambda: button_click('3'))
button_4 = Button(window, text="4", padx=40, pady=30,command=lambda: button_click('4'))
button_5 = Button(window, text="5", padx=40, pady=30,command=lambda: button_click('5'))
button_6 = Button(window, text="6", padx=40, pady=30,command=lambda: button_click('6'))
button_7 = Button(window, text="7", padx=40, pady=30,command=lambda: button_click('7'))
button_8 = Button(window, text="8", padx=40, pady=30,command=lambda: button_click('8'))
button_9 = Button(window, text="9", padx=40, pady=30,command=lambda: button_click('9'))
button_0 = Button(window, text="0", padx=40, pady=30,command=lambda: button_click('0'))
button_add = Button(window, text="+", padx=45, pady=30,command= addition)
button_sub = Button(window, text="-", padx=45, pady=30,command= subtraction)
button_clear = Button(window, text="Clear", padx=30, pady=30,command= clear)
button_equal_to = Button(window, text="=", padx=39, pady=30,command= equal_to)

button_9.grid(row=1, column=2)
button_8.grid(row=1, column=1)
button_7.grid(row=1, column=0)
button_6.grid(row=2, column=2)
button_5.grid(row=2, column=1)
button_4.grid(row=2, column=0)
button_3.grid(row=3, column=2)
button_2.grid(row=3, column=1)
button_1.grid(row=3, column=0)
button_0.grid(row=4, column=1)
button_clear.grid(row=4, column=2)
button_equal_to.grid(row=4, column=0)
button_add.grid(row=1, column=3)
button_sub.grid(row =2, column=3)

window.mainloop()
