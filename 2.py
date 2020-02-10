import tkinter as tk
from tkinter import ttk


win = tk.Tk()        
win.title("1.2")  

# Modify adding a Label
a = ttk.Label(win, text="")
a.grid(column=0, row=0)

# Modified Button Click Function
def click(): 
    win.destroy()

def hello(): 
    a.configure(text='Hello, world! ')


# Adding a Button
action = ttk.Button(win, text="Закрити", command=click)   
action.grid(column=1, row=1)

action = ttk.Button(win, text="Привітання", command=hello)   
action.grid(column=0, row=1)   
win.mainloop()
