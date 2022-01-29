import tkinter as tk
from tkinter.constants import DISABLED
from typing import Match
import math

root = tk.Tk()
root.title("Calculator")
root.wm_iconbitmap(r"C:\Users\Samarth Pachchigar\Downloads\calculator.ico")

e = tk.Entry(root, width=50,
                      fg = '#37d3ff',
                      bg = '#757C88',
                      bd =  10, 
                      highlightthickness=4, 
                      highlightcolor="#FFFFFF", 
                      highlightbackground="#FFFFFF", 
                      borderwidth=4)
e.grid(row=0, column=0, columnspan=3,padx=10,pady=10)

def button_click(number ):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, tk.END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, tk.END)
def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, tk.END)
def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, tk.END)
def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, tk.END)


def button_equal():

    second_number = e.get() 
    e.delete(0, tk.END)

    if math == "addition":
         e.insert(0, f_num + int(second_number)) 
    elif math == "subtraction":
         e.insert(0, f_num - float(second_number))
    elif math == "multiplication":
         e.insert(0, f_num * int(second_number))
    elif math == "division":
         e.insert(0, f_num / float(second_number))




   



#button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_1 = tk.Button(root, text = '1',
                      fg = '#FFFFFF',
                      bg = '#000000',
                      bd =  10,
                      padx=40,
                      pady=20,
                      command=lambda: button_click(1), 
                      highlightthickness=4, 
                      highlightcolor="#37d3ff", 
                      highlightbackground="#37d3ff", 
                      borderwidth=4)
#button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_2 = tk.Button(root, text = '2',
                      fg = '#FFFFFF',
                      bg = '#000000',
                      bd =  10,
                      padx=40,
                      pady=20,
                      command=lambda: button_click(2), 
                      highlightthickness=4, 
                      highlightcolor="#37d3ff", 
                      highlightbackground="#37d3ff", 
                      borderwidth=4)
#button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_3 = tk.Button(root, text = '3',
                      fg = '#FFFFFF',
                      bg = '#000000',
                      bd =  10,
                      padx=40,
                      pady=20,
                      command=lambda: button_click(3), 
                      highlightthickness=4, 
                      highlightcolor="#37d3ff", 
                      highlightbackground="#37d3ff", 
                      borderwidth=4)
#button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_4 = tk.Button(root, text = '4',
                      fg = '#FFFFFF',
                      bg = '#000000',
                      bd =  10,
                      padx=40,
                      pady=20,
                      command=lambda: button_click(4), 
                      highlightthickness=4, 
                      highlightcolor="#37d3ff", 
                      highlightbackground="#37d3ff", 
                      borderwidth=4)
#button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_5 = tk.Button(root, text = '5',
                      fg = '#FFFFFF',
                      bg = '#000000',
                      bd =  10,
                      padx=40,
                      pady=20,
                      command=lambda: button_click(5), 
                      highlightthickness=4, 
                      highlightcolor="#37d3ff", 
                      highlightbackground="#37d3ff", 
                      borderwidth=4)
#button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_6 = tk.Button(root, text = '6',
                      fg = '#FFFFFF',
                      bg = '#000000',
                      bd =  10,
                      padx=40,
                      pady=20,
                      command=lambda: button_click(6), 
                      highlightthickness=4, 
                      highlightcolor="#37d3ff", 
                      highlightbackground="#37d3ff", 
                      borderwidth=4)
#button_7= tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_7 = tk.Button(root, text = '7',
                      fg = '#FFFFFF',
                      bg = '#000000',
                      bd =  10,
                      padx=40,
                      pady=20,
                      command=lambda: button_click(7), 
                      highlightthickness=4, 
                      highlightcolor="#37d3ff", 
                      highlightbackground="#37d3ff", 
                      borderwidth=4)
#button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_8 = tk.Button(root, text = '8',
                      fg = '#FFFFFF',
                      bg = '#000000',
                      bd =  10,
                      padx=40,
                      pady=20,
                      command=lambda: button_click(8), 
                      highlightthickness=4, 
                      highlightcolor="#37d3ff", 
                      highlightbackground="#37d3ff", 
                      borderwidth=4)
#button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_9 = tk.Button(root, text = '9',
                      fg = '#FFFFFF',
                      bg = '#000000',
                      bd =  10,
                      padx=40,
                      pady=20,
                      command=lambda: button_click(9), 
                      highlightthickness=4, 
                      highlightcolor="#37d3ff", 
                      highlightbackground="#37d3ff", 
                      borderwidth=4)
#button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_0 = tk.Button(root, text = '0',
                      fg = '#FFFFFF',
                      bg = '#000000',
                      bd =  10,
                      padx=40,
                      pady=20,
                      command=lambda: button_click(0), 
                      highlightthickness=4, 
                      highlightcolor="#37d3ff", 
                      highlightbackground="#37d3ff", 
                      borderwidth=4)
#button_add = tk.Button(root, text="+", padx=39, pady=20, command=button_add)
button_add = tk.Button(root, text = '+',
                      fg = '#FFFFFF',
                      bg = '#000000',
                      bd =  10, 
                      padx=39,
                      pady=20,
                      command=button_add,
                      highlightthickness=4, 
                      highlightcolor="#37d3ff", 
                      highlightbackground="#37d3ff", 
                      borderwidth=4)
#button_subtract = tk.Button(root, text="-", padx=39, pady=20, command=button_subtract)
button_subtract = tk.Button(root, text = '-',
                      fg = '#FFFFFF',
                      bg = '#000000',
                      bd =  10, 
                      padx=39,
                      pady=20,
                      command=button_subtract,
                      highlightthickness=4, 
                      highlightcolor="#37d3ff", 
                      highlightbackground="#37d3ff", 
                      borderwidth=4)
#button_multiply = tk.Button(root, text="*", padx=39, pady=20, command=button_multiply)
button_multiply = tk.Button(root, text = '*',
                      fg = '#FFFFFF',
                      bg = '#000000',
                      bd =  10,
                      padx=39,
                      pady=20,
                      command=button_multiply, 
                      highlightthickness=4, 
                      highlightcolor="#37d3ff", 
                      highlightbackground="#37d3ff", 
                      borderwidth=4)
#button_divide = tk.Button(root, text="/", padx=39, pady=20, command=button_divide)
button_divide = tk.Button(root, text = '/',
                      fg = '#FFFFFF',
                      bg = '#000000',
                      bd =  10,
                      padx=39,
                      pady=20,
                      command=button_divide, 
                      highlightthickness=4, 
                      highlightcolor="#37d3ff", 
                      highlightbackground="#37d3ff", 
                      borderwidth=4)
#button_equal =  tk.Button(root, text="=", padx=91, pady=20, command= button_equal)
button_equal = tk.Button(root, text = '=',
                      fg = '#FFFFFF',
                      bg = '#000000',
                      bd =  10,
                      padx=91,
                      pady=20,
                      command=button_equal, 
                      highlightthickness=4, 
                      highlightcolor="#37d3ff", 
                      highlightbackground="#37d3ff", 
                      borderwidth=4)
#button_clear =  tk.Button(root, text="CLEAR", padx=79, pady=20, command=button_clear)
button_clear = tk.Button(root, text = 'CLEAR',
                      fg = '#FFFFFF',
                      bg = '#48AAAD',
                      bd =  10,
                      padx=79,
                      pady=20,
                      command=button_clear, 
                      highlightthickness=4, 
                      highlightcolor="#37d3ff", 
                      highlightbackground="#37d3ff", 
                      borderwidth=4)

#Put buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=5, column=1, columnspan=2)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)





root.mainloop()