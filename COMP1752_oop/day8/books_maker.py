from tkinter import *
from tkinter import messagebox as msb

from books import book as book_func
from gui import simple_gui

class book_maker(simple_gui):
	def __init__(self, title, width, height):
		super().__init__(title, width, height)
		self.load_books()

	def load_books(self):
		self.books = []
		python_intro = book_func("python_intro", "John Doe", 100)
		self.books.append(python_intro)
		java_intro = book_func("java_intro", "John Doe", 100)
		self.books.append(java_intro)
		c_sharp_intro = book_func("c_sharp_intro", "John Doe", 100)
		self.books.append(c_sharp_intro)
		for book in self.books:
			self.lst_books.insert(END, book.title)
	def create_widgets(self):
		lbl_book = Label(self.window, text="All")
		lbl_book.grid(row=0, column=0, sticky=W, pady=10)

		self.lst_books = Listbox(self.window)
		self.lst_books.grid(row=1, column=0, sticky=W, pady=10, rowspan=4)

		lbl_title = Label(self.window, text="Title")
		lbl_title.grid(row=1, column=1, sticky=E, pady=10)

		self.title = StringVar()
		txt_title = Entry(self.window, textvariable=self.title)
		txt_title.grid(row=1, column=2, sticky=W, pady=10, columnspan=3, padx=10)

		lbl_author = Label(self.window, text="author")
		lbl_author.grid(row=2, column=1, sticky=E, pady=10)

		self.author = StringVar()
		txt_author = Entry(self.window, textvariable=self.author)
		txt_author.grid(row=2, column=2, sticky=W, pady=10, columnspan=3, padx=10)

		lbl_price = Label(self.window, text="price")
		lbl_price.grid(row=3, column=1, sticky=E, pady=10)

		self.price = StringVar()
		txt_price = Entry(self.window, textvariable=self.price)
		txt_price.grid(row=3, column=2, sticky=W, pady=10, columnspan=3, padx=10)

		btn_add = Button(self.window, text="Add", command=None)
		btn_add.grid(row=4, column=2, sticky=W, pady=10, padx=10)

		btn_edit = Button(self.window, text="edit", command=None)
		btn_edit.grid(row=4, column=3, sticky=W, pady=10, padx=10)

		btn_delete = Button(self.window, text="delete", command=None)
		btn_delete.grid(row=4, column=4, sticky=W, pady=10, padx=10)

if __name__ == "__main__":
	gui = book_maker("book management", 600, 400)
	gui.run()
