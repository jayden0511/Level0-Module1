from tkinter import simpledialog,messagebox,Tk
Tk().withdraw()
a=simpledialog.askstring('title', 'when is your birthday')
if a=="june 5":
    messagebox.showinfo('cup', 'happy birthday')
else:
    messagebox.showinfo('iguana', 'merry unbirthday')
