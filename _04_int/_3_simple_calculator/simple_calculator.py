"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
from tkinter import simpledialog,messagebox,Tk
Tk().withdraw()


num3=simpledialog.askinteger('title 11', 'give me 1 random numbers')
num4=simpledialog.askinteger('title 12', 'give me 1 random numbers')
num5=simpledialog.askstring('title 13', 'would you like to add, subtract, multiply, or divide')
if num5=='add':
    messagebox.showinfo('title 14', num3+num4)
elif num5=='subtract':
    messagebox.showinfo('title 15', num3-num4)
elif num5=='multiply':
    messagebox.showinfo('title 16', num3*num4)
elif num5=='division':
    messagebox.showinfo('title 17', num3/num4)
