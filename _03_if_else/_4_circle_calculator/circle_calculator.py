from tkinter import simpledialog,messagebox,Tk
Tk().withdraw()
# Write a Python program that asks the user for the radius of a circle.
j=simpledialog.askinteger('title', 'whats the radius of a circle')
# Next, ask the user if they would like to calculate the area or circumference of a circle.
h=simpledialog.askstring('title 2', 'would you like to calculate the area or circumference of a circle')
# If they choose area, display the area of the circle using the radius.
if h == "area":
    messagebox.showinfo('title 3', 3.14*j*j)
# Otherwise, display the circumference of the circle using the radius.
elif h == 'circumference':
    messagebox.showinfo('title 3', 6.28*j)
#Area = πr^2
#Circumference = 2πr 
