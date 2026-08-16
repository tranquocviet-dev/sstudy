import tkinter as tk
import tkinter.scrolledtext as tkst

import message_manager as messages
import font_manager as fonts

class New_message:
	def __init__(self, window):
		self.window = window
		self.window.geometry("500x320")
		self.window.title("New message") #set window title
		sender_lbl = tk.Label(window, text="From:")
		sender_lbl.grid(row=0, column=0, sticky="E", padx=10, pady=10)

		self.sender_txt = tk.Entry(window, width=40)
		self.sender_txt.grid(row=0, column=1, columnspan=5, sticky="W", padx=10, pady=10)

		recipient_lbl = tk.Label(window, text="To:")
		recipient_lbl.grid(row=1, column=0, sticky="E", padx=10, pady=10)

		self.recipient_txt = tk.Entry(window, width=40)
		self.recipient_txt.grid(row=1, column=1, columnspan=5, sticky="W", padx=10, pady=10)

		subject_lbl = tk.Label(window, text="Subject:")
		subject_lbl.grid(row=2, column=0, sticky="E", padx=10, pady=10)

		self.subject_txt = tk.Entry(window, width=40)
		self.subject_txt.grid(row=2, column=1, columnspan=5, sticky="W", padx=10, pady=10)

		self.content_txt = tkst.ScrolledText(window, width=48, height=6, wrap="word")
		self.content_txt.grid(row=3, column=0, columnspan=6, sticky="W", padx=10, pady=10)

		subject_lbl = tk.Label(window, text="New priority (1-5):")
		subject_lbl.grid(row=4, column=0, columnspan=2, sticky="E", padx=10, pady=10)

		self.priority_txt = tk.Entry(window, width=3)
		self.priority_txt.grid(row=4, column=2, sticky="W", padx=10, pady=10)

		close_btn = tk.Button(window, text="Close", command=self.close)
		close_btn.grid(row=4, column=5, padx=10, pady=10)

		send_btn = tk.Button(window, text="Send", command=self.send)
		send_btn.grid(row=4, column=4, padx=10, pady=10)
	def close(self):
		self.window.destroy() # destroy the window
	def send(self):
		pass # placeholder for function declared later
	def delete(self):
		pass

if __name__ == "__main__":
	tkin = tk.Tk()
	fonts.configure()
	New_message(tkin)
	tkin.mainloop()
