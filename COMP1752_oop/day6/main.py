from tkinter import Tk, Label, Button
from tkinter import messagebox as msb

window = Tk()
window.title("simple gui")
window.geometry("300x200")

def button_click():
    msb.showinfo("information", "button was clicked")

label = Label(window, text="Hello world")
label.grid(row=0, column=0, padx=10, pady=10)
button = Button(window, text="text", command=button_click)
button.grid(row=1, column=1, padx=10, pady=10)

window.mainloop()
