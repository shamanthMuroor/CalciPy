#!/usr/bin/python

""" Calculator App """

import tkinter as tk
from tkinter import messagebox
import re

expression = "" 

def set_equation(n):
    global expression
    if len(expression) < 20:
        expression += n
        equation.set(expression)

def operator(op):
    listops = ["+", "-", "*", "/", "%"]
    global expression 
    if expression != "":
        if expression[-1] in listops:
            expression = expression[:-1]
    expression += op
    equation.set(expression)

def sploperator(op):
    """ Power(^), Root(√), Dot(.) """
    global expression 
    if expression != "":
        if expression[-1] == op:
            expression = expression[:-1]
    expression += op
    equation.set(expression)

def calc():
    try:  
        global expression
        listops = ["+", "-", "*", "/", "%", "^", "√"]
        if expression[-1] not in listops:
            if "^" in expression:
                expression = expression.replace("^", "**")
            if "√" in expression:
                x = expression.find("√")
                if expression[x+1:] in listops:
                    y = expression[x+1:].find(listops)
                    print(y)
                    expression = expression[:x] + expression[x+1:y] + "**(1/2)" + expression[y:]
                else:
                    expression = expression[:x] + expression[x+1:] + "**(1/2)"
            if "0" in expression:
                remzero = True
                while remzero:
                    if re.search(r"0(\d[\+\*\%\-\d]*)", expression):
                        expression = re.sub(r"0(\d[\+\*\%\-\d]*)", r"\1", expression)
                    else:
                        remzero = False
                    
            total = str(eval(expression)) 
            equation.set(total) 
            expression = total        
    except ValueError:
        messagebox.showerror("Warning","Check your input")
        expression = ""
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero error")
        expression = ""
                    
def clearinputs():
    global expression
    expression = ""
    equation.set("")

def delprev():
    global expression
    if expression != "":
        expression = expression[:-1]
    equation.set(expression)


calculator = tk.Tk()
calculator.title("Calculator")
calculator.minsize(450,540)
calculator.option_add("*font", "Arial 14 bold")
calculator.configure(bg="#252729", bd=10, relief='flat')
for row in range(7):               
    calculator.grid_rowconfigure(row, weight=1)
for col in range(4):               
    calculator.grid_columnconfigure(col, weight=1)
equation = tk.StringVar()
input_field = tk.Entry(calculator, textvariable=equation, justify="right", bd=0, bg="#252729", fg="#ffffff", font= "Arial 28 bold")
input_field.grid(row=0, column=0, columnspan=4, sticky="nsew")
equation.set(0) 

Bleftbracker = tk.Button(calculator, text="(", relief="flat", bg="#0e0f0f", fg="#f5f6fa", activebackground='#0097e6', activeforeground= "#000000", command=lambda: set_equation("("))
Brightbracker = tk.Button(calculator, text=")", relief="flat", bg="#0e0f0f", fg="#f5f6fa", activebackground='#0097e6', activeforeground= "#000000", command=lambda: set_equation(")"))
Bclear = tk.Button(calculator, text="AC", relief="flat", bg="#0e0f0f", fg="#f5f6fa", activebackground='#d63031', activeforeground= "#000000", command=clearinputs)
Bdel = tk.Button(calculator, text="del", relief="flat", bg="#0e0f0f", fg="#f5f6fa", activebackground='#d63031', activeforeground= "#000000", command=delprev)

Bpercent = tk.Button(calculator, text="%", relief="flat", bg="#0e0f0f", fg="#f5f6fa", activebackground='#0097e6', activeforeground= "#000000", command=lambda: operator("%"))
Bpower = tk.Button(calculator, text="^", relief="flat", bg="#0e0f0f", fg="#f5f6fa", activebackground='#0097e6', activeforeground= "#000000", command=lambda: sploperator("^"))
Broot = tk.Button(calculator, text="√", relief="flat", bg="#0e0f0f", fg="#f5f6fa", activebackground='#0097e6', activeforeground= "#000000", command=lambda: sploperator("√"))
Bdiv = tk.Button(calculator, text="/", relief="flat", bg="#0e0f0f", fg="#f5f6fa", activebackground='#0097e6', activeforeground= "#000000", command=lambda: operator("/"))

B7 = tk.Button(calculator, text="7", relief="flat", bg="#050505", fg="#f5f6fa", activebackground='#635f5f', activeforeground= "#000000", command=lambda: set_equation("7"))
B8 = tk.Button(calculator, text="8", relief="flat", bg="#050505", fg="#f5f6fa", activebackground='#635f5f', activeforeground= "#000000", command=lambda: set_equation("8"))
B9 = tk.Button(calculator, text="9", relief="flat", bg="#050505", fg="#f5f6fa", activebackground='#635f5f', activeforeground= "#000000", command=lambda: set_equation("9"))
Bmult = tk.Button(calculator, text="*", relief="flat", bg="#0e0f0f", fg="#f5f6fa", activebackground='#0097e6', activeforeground= "#000000", command=lambda: operator("*"))

B4 = tk.Button(calculator, text="4", relief="flat", bg="#050505", fg="#f5f6fa", activebackground='#635f5f', activeforeground= "#000000", command=lambda: set_equation("4"))
B5 = tk.Button(calculator, text="5", relief="flat", bg="#050505", fg="#f5f6fa", activebackground='#635f5f', activeforeground= "#000000", command=lambda: set_equation("5"))
B6 = tk.Button(calculator, text="6", relief="flat", bg="#050505", fg="#f5f6fa", activebackground='#635f5f', activeforeground= "#000000", command=lambda: set_equation("6"))
Bminus = tk.Button(calculator, text="-", relief="flat", bg="#0e0f0f", fg="#f5f6fa", activebackground='#0097e6', activeforeground= "#000000", command=lambda: operator("-"))

B1 = tk.Button(calculator, text="1", relief="flat", bg="#050505", fg="#f5f6fa", activebackground='#635f5f', activeforeground= "#000000", command=lambda: set_equation("1"))
B2 = tk.Button(calculator, text="2", relief="flat", bg="#050505", fg="#f5f6fa", activebackground='#635f5f', activeforeground= "#000000", command=lambda: set_equation("2")) 
B3 = tk.Button(calculator, text="3", relief="flat", bg="#050505", fg="#f5f6fa", activebackground='#635f5f', activeforeground= "#000000", command=lambda: set_equation("3"))
Bplus = tk.Button(calculator, text="+", relief="flat", bg="#0e0f0f", fg="#f5f6fa", activebackground='#0097e6', activeforeground= "#000000", command=lambda: operator("+"))

B0 = tk.Button(calculator, text="0", relief="flat", bg="#050505", fg="#f5f6fa", activebackground='#635f5f', activeforeground= "#000000", command=lambda: set_equation("0"))
Bdot = tk.Button(calculator, text=".", relief="flat", bg="#0e0f0f", fg="#f5f6fa", activebackground='#0097e6', activeforeground= "#000000", command=lambda: sploperator("."))
Bequal = tk.Button(calculator, text="=", relief="flat", bg="#0e0f0f", fg="#f5f6fa", activebackground='#0097e6', activeforeground= "#000000", command=calc)




Bleftbracker.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
Brightbracker.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
Bclear.grid(row=1, column=2, sticky="nsew", padx=2, pady=2)
Bdel.grid(row=1, column=3, sticky="nsew", padx=2, pady=2)

Bpercent.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)
Bpower.grid(row=2, column=1, sticky="nsew", padx=2, pady=2)
Broot.grid(row=2, column=2, sticky="nsew", padx=2, pady=2)
Bdiv.grid(row=2, column=3, sticky="nsew", padx=2, pady=2)


B7.grid(row=3, column=0, sticky="nsew", padx=2, pady=2)
B8.grid(row=3, column=1, sticky="nsew", padx=2, pady=2)
B9.grid(row=3, column=2, sticky="nsew", padx=2, pady=2)
Bmult.grid(row=3, column=3, sticky="nsew", padx=2, pady=2)

B4.grid(row=4, column=0, sticky="nsew", padx=2, pady=2)
B5.grid(row=4, column=1, sticky="nsew", padx=2, pady=2)  
B6.grid(row=4, column=2, sticky="nsew", padx=2, pady=2)
Bminus.grid(row=4, column=3, sticky="nsew", padx=2, pady=2)

B1.grid(row=5, column=0, sticky="nsew", padx=2, pady=2)
B2.grid(row=5, column=1, sticky="nsew", padx=2, pady=2)
B3.grid(row=5, column=2, sticky="nsew", padx=2, pady=2)
Bplus.grid(row=5, column=3, sticky="nsew", padx=2, pady=2)

B0.grid(row=6, column=0, columnspan=2, sticky="nsew", padx=2, pady=2)
Bdot.grid(row=6, column=2, sticky="nsew", padx=2, pady=2)
Bequal.grid(row=6, column=3, sticky="nsew", padx=2, pady=2)


calculator.mainloop()