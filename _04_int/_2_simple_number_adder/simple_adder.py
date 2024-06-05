"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""
from tkinter import simpledialog,messagebox,Tk
Tk().withdraw()

num1=simpledialog.askinteger('title 8', 'give me 1 random numbers')
num2=simpledialog.askinteger('title 9', 'give me 1 random numbers')
messagebox.showinfo('title 10', num1+num2)
