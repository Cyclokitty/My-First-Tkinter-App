import tkinter as tk
from tkinter import ttk


# global variables
count = 0
padx = 10
pady = 10
textColour = '#ff0080'
backgroundColour = '#fff2cc'

# button function call
def btn_function():
    global count
    count += 1
    #print(f'Clicky clicky button was pressed {count} times!')
    clickLbl.configure(text=f'Button was clicked {count} times!!!')

window = tk.Tk()

# setting the size of the window
window.geometry('900x500')
window.title('My First Tkinter App')
window.configure(bg = backgroundColour)

# title lable
lbl = tk.Label(
    window, 
    text='Hello, World!', 
    font=('Arial Bold', 30),
    foreground=textColour,
    background=backgroundColour
    )
lbl.pack(padx=padx, pady=pady)

# button
btn = tk.Button(
    window,
    text = 'Clicky clicky!',
    width = 40,
    foreground=textColour,
    highlightbackground=backgroundColour,
    command = btn_function
)
btn.pack(padx=padx, pady=pady)

# text label showing number of button clicks
clickLbl = tk.Label(
    window,
    foreground = textColour,
    background = backgroundColour,
    font = ('Arial', 30),
    text = 'See how many clicks HERE!'
)
clickLbl.pack(padx=padx, pady=pady)

window.mainloop()

