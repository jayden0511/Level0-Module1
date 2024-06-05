"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
from tkinter import simpledialog,messagebox,Tk
Tk().withdraw()

a=0
y=simpledialog.askstring('title 6', 'do you have eyes')
if y=='yes':
    a+=1
y=simpledialog.askstring('title 6', 'do you like video games')
if y=='yes':
    a+=1
y=simpledialog.askstring('title 6', 'do you have any devices at home')
if y=='yes':
    a+=1
messagebox.showinfo('title 7', a)
