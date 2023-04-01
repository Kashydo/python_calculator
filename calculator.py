from tkinter import *

# import os
# import sys


root = Tk()
root.title("Kalkulator")
window = Entry(root, width=50, borderwidth=5)
window.grid(row=0, column=1, columnspan=4, padx=10, pady=10)

equation = []
total = 0


def button_click(number):
    global total
    if total == 0:
        current = window.get()
        window.delete(0, END)
        num = current + number
        window.insert(0, num)
    else:
        window.delete(0, END)
        current = window.get()
        num = current + number
        window.insert(0, num)
        total = 0


def button_math_sign(sign):
    global total
    equation.append(window.get())
    window.delete(0, END)
    total = eval(" ".join(str(x) for x in equation))
    equation.clear()
    equation.append(total)
    equation.append(sign)
    window.insert(0, total)


def clr():
    global total
    window.delete(0, END)
    total = 0
    equation.clear()


def equal():
    equation.append(window.get())
    window.delete(0, END)
    total = eval(" ".join(str(x) for x in equation))
    equation.clear()
    window.insert(0, total)


# butons

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click("1"))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click("2"))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click("3"))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click("4"))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click("5"))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click("6"))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click("7"))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click("8"))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click("9"))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click("0"))
button_clr = Button(root, text="CLR", padx=40, pady=20, command=lambda: clr())
button_plus = Button(
    root, text="+", padx=40, pady=20, command=lambda: button_math_sign("+")
)
button_equal = Button(root, text="=", padx=40, pady=20, command=lambda: equal())
button_multi = Button(
    root, text="x", padx=40, pady=20, command=lambda: button_math_sign("*")
)
button_division = Button(
    root, text="/", padx=40, pady=20, command=lambda: button_math_sign("/")
)
button_sub = Button(
    root, text="-", padx=40, pady=20, command=lambda: button_math_sign("-")
)


# button grid
button_7.grid(row=2, column=1)
button_8.grid(row=2, column=2)
button_9.grid(row=2, column=3)
button_multi.grid(row=2, column=4)
button_4.grid(row=3, column=1)
button_5.grid(row=3, column=2)
button_6.grid(row=3, column=3)
button_division.grid(row=3, column=4)
button_1.grid(row=4, column=1)
button_2.grid(row=4, column=2)
button_3.grid(row=4, column=3)
button_sub.grid(row=4, column=4)
button_clr.grid(row=5, column=1)
button_0.grid(row=5, column=2)
button_equal.grid(row=5, column=3)
button_plus.grid(row=5, column=4)


root.mainloop()
