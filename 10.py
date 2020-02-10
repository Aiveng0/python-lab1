import tkinter as tk
from tkinter import ttk


win = tk.Tk()        
win.title("1.1")  

# Modify adding a Label
ttk.Label(win, text="Моя перша програма").grid(column=0, row=0)

# Modified Button Click Function
def click(): 
    win.destroy()


# Adding a Button
action = ttk.Button(win, text="Close", command=click)   
action.grid(column=0, row=1)   
win.mainloop()
