import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import messagebox

import message_manager as messages
import font_manager as fonts
import dialog_msg


def set_text(text_area, content):
	text_area["state"] = "normal"
	text_area.delete("1.0", tk.END)
	text_area.insert(1.0, content)
	text_area["state"] = "disabled"


class Label_message:
	def __init__(self, window):
		self.window = window
		self.window.geometry("640x350")
		self.window.title("Label Messages")

		# UI declaration
		list_messages_btn = tk.Button(window, text="List All Messages Labeled:", command=self.list_messages_labeled)
		list_messages_btn.grid(row=0, column=0, padx=10, pady=10)

		self.label_txt = tk.Entry(window, width=6)
		self.label_txt.grid(row=0, column=2, padx=10, pady=10)

		new_message_btn = tk.Button(window, text="Add Label to Messages:", command=self.add_label)
		new_message_btn.grid(row=0, column=3, padx=10, pady=10)

		self.msg_id = tk.Entry(window, width=3)
		self.msg_id.grid(row=0, column=4, padx=10, pady=10)

		self.list_txt = tkst.ScrolledText(window, width=60, height=12, wrap="none")
		self.list_txt.grid(row=1, column=0, columnspan=5, sticky="W", padx=10, pady=10)

		self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
		self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)
		self.close_btn = tk.Button(window, text="Close", command=self.close)
		self.close_btn.grid(row=2, column=4, padx=10, pady=10)

		# call the function to list all messages upon init
		self.list_messages_labeled()

	def list_messages(self):
		message_list = messages.list_all()
		set_text(self.list_txt, message_list)
		self.status_lbl.configure(text="List Messages button was clicked!")

	def add_label(self):
		label_string = self.label_txt.get()
		msg_id_string = self.msg_id.get()
		if msg_id_string != '' and 0 <= int(msg_id_string) <= len(messages.messages):
			messages.set_label(int(msg_id_string), label_string)
			self.list_messages_labeled()
		else:
			dialog_msg.dialog("ERROR", "Label box is empty!", self.window)
			pass
		self.status_lbl.configure(text="Add Label button was clicked!")

	def list_messages_labeled(self):
		label_string = self.label_txt.get()
		message_list = messages.list_all_adjusted() if label_string == '' else messages.list_all_adjusted(label=label_string)
		set_text(self.list_txt, message_list)
		self.status_lbl.configure(text="List Messages Labeled was clicked!")

	def close(self):
		self.window.destroy()



if __name__ == "__main__":
	window = tk.Tk()
	fonts.configure()
	Label_message(window)
	window.mainloop()
