
from tkinter import Tk, Label, Button, Entry, StringVar
from tkinter import messagebox as msb

from gui1 import Window

class Payment(Window):
    def __init__(self):
        super().__init__("GUI 3", 300, 200)
    def create_widgets(self):
        lbl_price = Label(self.window, text="Product Price")
        lbl_price.grid(row=0, column=0, padx=10, pady=10)

        self.price = StringVar()
        self.txt_price = Entry(self.window, textvariable=self.price)
        self.txt_price.grid(row=0, column=1, padx=10, pady=10)

        lbl_quantity = Label(self.window, text="Quantity")
        lbl_quantity.grid(row=1, column=0, padx=10, pady=10)

        self.quantity = StringVar()
        self.txt_quantity = Entry(self.window, textvariable=self.quantity)
        self.txt_quantity.grid(row=1, column=1, padx=10, pady=10)

        lbl_commision = Label(self.window, text="commision")
        lbl_commision.grid(row=2, column=0, padx=10, pady=10)

        self.commision = StringVar()
        self.txt_commision = Entry(self.window, textvariable=self.commision)
        self.txt_commision.grid(row=2, column=1, padx=10, pady=10)

        btn_calc = Button(self.window, text="payment", command=self.on_lick)
        btn_calc.grid(row=3, column=1, padx=10, pady=10)

    def on_lick(self):
        pri = float(self.price.get())
        quan = float(self.quantity.get())
        com = float(self.commision.get())
        calced = pri*quan*(100-com)
        msb.showinfo("info", f"Total Payment = {calced}")

if __name__ == "__main__":
    swin = Payment()
    swin.run()
