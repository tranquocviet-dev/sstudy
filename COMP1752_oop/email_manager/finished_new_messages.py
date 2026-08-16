import tkinter as tk
import tkinter.messagebox
import tkinter.scrolledtext as tkst

import message_manager as messages
import font_manager as fonts
from dialog_msg import dialog

class New_message:
	def __init__(self, window):
		self.window = window
		self.window.geometry("500x400")
		self.window.title("New message") #set window title
		sender_lbl = tk.Label(window, text="From:")
		sender_lbl.grid(row=0, column=0, sticky="E", padx=10, pady=10)

		self.sender_txt = tk.Entry(window, width=30)
		self.sender_txt.grid(row=0, column=1, columnspan=6, sticky="W", padx=10, pady=10)

		recipient_lbl = tk.Label(window, text="To:")
		recipient_lbl.grid(row=1, column=0, sticky="E", padx=10, pady=10)

		self.recipient_txt = tk.Entry(window, width=30)
		self.recipient_txt.grid(row=1, column=1, columnspan=6, sticky="W", padx=10, pady=10)

		subject_lbl = tk.Label(window, text="Subject:")
		subject_lbl.grid(row=2, column=0, sticky="E", padx=10, pady=10)

		self.subject_txt = tk.Entry(window, width=30)
		self.subject_txt.grid(row=2, column=1, columnspan=6, sticky="W", padx=10, pady=10)

		self.content_txt = tkst.ScrolledText(window, width=48, height=8, wrap="word")
		self.content_txt.grid(row=3, column=0, columnspan=6, sticky="W", padx=10, pady=10)

		close_btn = tk.Button(window, text="Close", command=self.close)
		close_btn.grid(row=4, column=5, padx=10, pady=10)

		send_btn = tk.Button(window, text="Send", command=self.send)
		send_btn.grid(row=4, column=4, padx=10, pady=10)

		self.status_lbl = tk.Label(window, text="", font=("Helvetica", 12))
		self.status_lbl.grid(row=5, column=0, columnspan=4, sticky="W", padx=10, pady=10)
	def close(self):
		self.window.destroy() # destroy the window
	def send(self):
		sender_txt_string = str(self.sender_txt.get())
		recipient_txt_string = str(self.recipient_txt.get())
		subject_txt_string = str(self.subject_txt.get())
		content_txt_string = str(self.content_txt.get("1.0", "end-1c"))
		if sender_txt_string == '' or recipient_txt_string == '':
			dialog("ERROR!", "Either Sender or Recipient is not entered!", self.window)
			pass
		elif "@" not in sender_txt_string:
			dialog("ERROR!", "Sender is not a mail!", self.window)
			pass
		elif "@" not in recipient_txt_string:
			dialog("ERROR!", "Recipient is not a mail!", self.window)
			pass
		else:
			messages.new_message(sender_txt_string, recipient_txt_string, subject_txt_string, content_txt_string) if subject_txt_string != '' else messages.new_message(sender_txt_string, recipient_txt_string, "(No Subject)", content_txt_string)
			self.window.destroy()
if __name__ == "__main__":
	tkin = tk.Tk()
	fonts.configure()
	New_message(tkin)
	tkin.mainloop()
