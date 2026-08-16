import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import messagebox

from dialog_msg import dialog
from theming import apply_theme_palette, MOCHA, DEFAULT_THEME, toggle_theme
import message_manager as messages
import font_manager as fonts
from read_message import ReadMessage
from finished_new_messages import New_message
from finished_label_messages import Label_message


def set_text(text_area, content):
	text_area["state"] = "normal"
	text_area.delete("1.0", tk.END)
	text_area.insert(1.0, content)
	text_area["state"] = "disabled"


class EmailManager():
	def __init__(self, window):
		self.window = window
		self.window.geometry("720x380")
		self.window.title("Email Manager")

		list_messages_btn = tk.Button(window, text="List Messages", command=self.list_messages)
		list_messages_btn.grid(row=0, column=0, padx=10, pady=10)

		read_message_btn = tk.Button(window, text="Read Message:", command=self.read_message)
		read_message_btn.grid(row=0, column=1, padx=10, pady=10)

		self.id_txt = tk.Entry(window, width=3)
		self.id_txt.grid(row=0, column=2, padx=10, pady=10)

		new_message_btn = tk.Button(window, text="New Message", command=self.new_message)
		new_message_btn.grid(row=0, column=3, padx=10, pady=10)

		label_messages_btn = tk.Button(window, text="Label Messages", command=self.label_messages)
		label_messages_btn.grid(row=0, column=4, padx=10, pady=10)

		self.list_txt = tkst.ScrolledText(window, width=60, height=12, wrap="none")
		self.list_txt.grid(row=1, column=0, columnspan=5, sticky="W", padx=10, pady=10)

		self.sender_lbl = tk.Label(window, text="Sender:")
		self.sender_lbl.grid(row=2, column=0, sticky="E", padx=10, pady=10)
		self.sender_txt = tk.Entry(window, width=10)
		self.sender_txt.grid(row=2, column=1, padx=10, pady=10)

		self.subject_lbl = tk.Label(window, text="Subject:")
		self.subject_lbl.grid(row=2, column=2, sticky="E", padx=10, pady=10)
		self.subject_txt = tk.Entry(window, width=10)
		self.subject_txt.grid(row=2, column=3, padx=10, pady=10)
		self.status_lbl = tk.Label(window, text="")
		self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="W", padx=10, pady=10)
		self.theme_toggle = tk.Button(window, text="Toggle Theme", command=lambda: toggle_theme(window))
		self.theme_toggle.grid(row=2, column=4, sticky="W", padx=10, pady=10)
		self.list_messages()

	def read_message(self):
		message_id_string = self.id_txt.get()
		valid = False
		if len(message_id_string) > 0:
			message_id = int(message_id_string)
			sender = messages.get_sender(message_id)
			if sender is not None:
				ReadMessage(tk.Toplevel(window), message_id)
				valid = True
		if not valid:
			dialog("WARNING", "You must select a valid message ID", window)
		self.status_lbl.configure(text="Read Message button was clicked!")

	def list_messages(self):
		sender_string = self.sender_txt.get()
		subject_string = self.subject_txt.get()
		if not sender_string:  # Catches '' or None
			sender_string = None
		if not subject_string:  # Catches '' or None
			subject_string = None
		message_list = messages.list_all_adjusted(sender=sender_string, subject=subject_string)
		set_text(self.list_txt, message_list)
		self.status_lbl.configure(text="List Messages button was clicked!")

	def new_message(self):
		New_message(tk.Toplevel(window))
		self.status_lbl.configure(text="New Message button was clicked!")

	def label_messages(self):
		Label_message(tk.Toplevel(window))

if __name__ == "__main__":
	window = tk.Tk()
	fonts.configure()
	EmailManager(window)
	window.mainloop()
