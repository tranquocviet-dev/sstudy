from tkinter import Tk, Label, Button, Entry, StringVar
from tkinter import messagebox as msb

from gui1 import Window

class SimpleGui(Window):
    def __init__(self):
        super().__init__("GUI 3", 300, 200)
    def create_widgets(self):
        label_salary = Label(self.window, text="Salary")
        label_salary.grid(row=0, column=0, padx=10, pady=10)

        self.salary = StringVar()
        self.txt_salary = Entry(self.window, textvariable=self.salary)
        self.txt_salary.grid(row=0, column=1, padx=10, pady=10)

        lbl_tax = Label(self.window, text="Tax Rate (%):")
        lbl_tax.grid(row=1, column=0, padx=10, pady=10)

        self.tax_rate = StringVar()
        self.txt_tax = Entry(self.window, textvariable=self.tax_rate)
        self.txt_tax.grid(row=1, column=1, padx=10, pady=10)

        btn_calc = Button(self.window, text="calculate", command=self.on_lick)
        btn_calc.grid(row=2, column=1, padx=10, pady=10)

    def on_lick(self):
        sal = float(self.salary.get())
        tax = float(self.tax_rate.get())
        calced = sal*tax/100
        msb.showinfo("info", calced)

if __name__ == "__main__":
    swin = SimpleGui()
    swin.run()
