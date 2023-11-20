from tkinter import *
from tkinter import messagebox

def click():
    messagebox.showinfo(title="info", message="user")
    messagebox.showwarning(title="WARNING", message="VIREN")
    messagebox.showerror(title="ERROR", message="Schief gegehen")

if messagebox.askokcancel(title="askokcancel", message="Willst du die Zeit"):
    print("Ja,gebraucht")
else:
    print("Nein, Danke!")

window= Tk()
button= Button(window, command="Click", text="Click me!")
button.pack()
window.mainloop()