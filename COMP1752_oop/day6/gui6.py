from tkinter import Label, Radiobutton, IntVar, StringVar, Entry, Button
from tkinter import messagebox as msb

from gui1 import Window

class Hotel1(Window):
    def __init__(self):
        super().__init__("GUI 3", 600, 600)
    def create_widgets(self):
        lbl_room = Label(self.window, text="Room")
        lbl_room.grid(row=0, column=0, padx=10, pady=10)
        self.option = IntVar()
        self.option.set(1)
        rd_pizza = Radiobutton(self.window, text="Deluxe", value=1, variable=self.option)
        rd_pizza.grid(row=0, column=1, padx=10, pady=10)

        rd_burger = Radiobutton(self.window, text="Garden View", value=2, variable=self.option)
        rd_burger.grid(row=0, column=2, padx=10, pady=10)

        rd_sushi = Radiobutton(self.window, text="Ocean", value=3, variable=self.option)
        rd_sushi.grid(row=0, column=3, padx=10, pady=10)

        lbl_night = Label(self.window, text="Night")
        lbl_night.grid(row=1, column=0, padx=10, pady=10)

        self.night_deluxe = StringVar()
        entry_night_deluxe = Entry(self.window, textvariable=self.night_deluxe)
        entry_night_deluxe.grid(row=1, column=1, padx=10, pady=10)

        self.night_garden = StringVar()
        entry_night_garden = Entry(self.window, textvariable=self.night_garden)
        entry_night_garden.grid(row=1, column=2, padx=10, pady=10)

        self.night_ocean = StringVar()
        entry_night_ocean = Entry(self.window, textvariable=self.night_ocean)
        entry_night_ocean.grid(row=1, column=3, padx=10, pady=10)

        lbl_extra = Label(self.window, text="Extra")
        lbl_extra.grid(row=2, column=0, padx=10, pady=10)

        self.extra_deluxe = StringVar()
        entry_extra_deluxe = Entry(self.window, textvariable=self.extra_deluxe)
        entry_extra_deluxe.grid(row=2, column=1, padx=10, pady=10)

        self.extra_garden = StringVar()
        entry_extra_garden = Entry(self.window, textvariable=self.extra_garden)
        entry_extra_garden.grid(row=2, column=2, padx=10, pady=10)

        self.extra_ocean = StringVar()
        entry_extra_ocean = Entry(self.window, textvariable=self.extra_ocean)
        entry_extra_ocean.grid(row=2, column=3, padx=10, pady=10)

        btn_calculate = Button(self.window, text="Calculate", command=self.on_calc)
        btn_calculate.grid(row=3, column=0, padx=10, pady=10)

    def on_calc(self):
        op = int(self.option.get())
        if op == 1:
            nd = int(self.night_deluxe.get())
            ed = int(self.extra_deluxe.get())
            total = (80*nd)+ed
            msb.showinfo("Calculation Finished", f"Total Cost is {total}")
        elif op == 2:
            ng = int(self.night_garden.get())
            eg = int(self.extra_garden.get())
            total = (100*ng)+eg
            msb.showinfo("Calculation Finished", f"Total Cost is {total}")
        elif op == 3:
            no = int(self.night_ocean.get())
            eo = int(self.extra_ocean.get())
            total = (120*no)+eo
            msb.showinfo("Calculation Finished", f"Total Cost is {total}")
if __name__ == "__main__":
    swin = Hotel1()
    swin.run()
