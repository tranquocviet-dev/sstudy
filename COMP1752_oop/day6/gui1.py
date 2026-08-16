from tkinter import Tk, Label, Button
from tkinter import messagebox as msb

class Window():
    def __init__(self, title, width, height):
        self.window = Tk()
        self.window.title(title)
        self.window.geometry(f"{width}x{height}")
        self.create_widgets()

    def create_widgets():
        pass

    def run(self):
        self.window.mainloop()
