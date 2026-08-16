from tkinter import Label, Radiobutton, IntVar, StringVar, Entry
from tkinter import messagebox as msb

from gui1 import Window

class Food(Window):
	def __init__(self):
		super().__init__("GUI 3", 300, 200)

	def create_widgets(self):
		lbl_combo = Label(self.window, text="Select a combo:")
		lbl_combo.grid(row=0, column=0, padx=10, pady=10)

		self.combo_var = IntVar()
		self.combo_var.set(1)
		rd_pizza = Radiobutton(
			self.window,
			text="Pizza",
			value=1,
			variable=self.combo_var,
			command=self.rd_combo_click,
		)
		rd_pizza.grid(row=1, column=0, padx=10, pady=10)

		rd_burger = Radiobutton(
			self.window,
			text="burger",
			value=2,
			variable=self.combo_var,
			command=self.rd_combo_click,
		)
		rd_burger.grid(row=2, column=0, padx=10, pady=10)

		rd_sushi = Radiobutton(
			self.window,
			text="sushi",
			value=3,
			variable=self.combo_var,
			command=self.rd_combo_click,
		)
		rd_sushi.grid(row=3, column=0, padx=10, pady=10)

		lbl_payment = Label(self.window, text="Payment:")
		lbl_payment.grid(row=4, column=0, padx=10, pady=10)
		self.paymentvar = StringVar()
		self.paymentvar.set("$10")
		txt_payment = Entry(self.window, textvariable=self.paymentvar)
		txt_payment.grid(row=4, column=2, padx=10, pady=10)

	def rd_combo_click(self):
		selected_combo = int(self.combo_var.get())
		if selected_combo == 1:
			self.paymentvar.set("$10")
		elif selected_combo == 2:
			self.paymentvar.set("$12")
		elif selected_combo == 3:
			self.paymentvar.set("$8")

if __name__ == "__main__":
	swin = Food()
	swin.run()
