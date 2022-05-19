#Dicegame GUI testing
import tkinter as tk
from tkinter import ttk, Tk, Text

def callback():
    print("Hello")


window= tk.Tk()
window.geometry("500x500")
window.title("Dicegame planning")
window.resizable(False,False)
title = tk.Label(
    window,
    text = "Dice Game",
    font = ("Cooper black", 40),
    fg = "blue",
    anchor = "n")

dicephoto = tk.PhotoImage(file = './Desktop/dice image.png')
dicelabel = ttk.Label(
    window,
    image = dicephoto,
    compound = "bottom"
)
dicelabel.pack()

hellobutton = ttk.Button(
    window,
    text = "Something",
    command = callback
)
exitbutton = ttk.Button(
    window,
    text= "Exit Program",
    command=lambda: window.quit()
)

title.pack(ipadx=20, ipady=10)
title.place(x = 250, y = 50, anchor = "center")

hellobutton.pack(ipadx=20, ipady=10)
hellobutton.place(x=250, y= 200, anchor = "center")

exitbutton.pack(ipadx = 20, ipady = 10)
exitbutton.place(x=250, y = 250, anchor = "center")

window.mainloop()

