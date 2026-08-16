from tkinter import Tk, Label, Button
from tkinter import messagebox as msb

from gui1 import Window

class SimpleGui(Window):
    def __init__(self):
        super().__init__("Simple GUI", 300, 200)
    def create_widgets(self):
        label = Label(self.window, text="Hello world")
        label.grid(row=0, column=0, padx=10, pady=10)

        button = Button(self.window, text="lick me", command=self.on_lick)
        button.grid(row=1, column=1, padx=10, pady=10)

    def on_lick(self):
        msb.showinfo("info", "licked")

if __name__ == "__main__":
    swin = SimpleGui()
    swin.run()
