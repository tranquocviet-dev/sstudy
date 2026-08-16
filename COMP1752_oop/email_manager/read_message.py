import tkinter as tk
import tkinter.scrolledtext as tkst

import message_manager as messages
import font_manager as fonts


class ReadMessage:
	# the code that runs on startup, usually handling definitions and declarations
	def __init__(self, window, message_id):
		self.message_id = message_id

		# define window options
		self.window = window # create new window
		self.window.geometry("500x320") # set window size
		self.window.title(f"Read Message {message_id}") #set window title
		
		sender_lbl = tk.Label(window, text="From:") # create "From:" label
		sender_lbl.grid(row=0, column=0, sticky="E", padx=10, pady=10) # place "From:" label

		self.sender_txt = tk.Entry(window, width=40) # create input box for sender
		self.sender_txt.grid(
			row=0, column=1, columnspan=5, sticky="W", padx=10, pady=10
		) # place input box inside window

		recipient_lbl = tk.Label(window, text="To:") # create "To:" label
		recipient_lbl.grid(row=1, column=0, sticky="E", padx=10, pady=10) # place "To:" label

		self.recipient_txt = tk.Entry(window, width=40) # create input box for recipient
		self.recipient_txt.grid(
			row=1, column=1, columnspan=5, sticky="W", padx=10, pady=10
		) # place input box for recipient

		subject_lbl = tk.Label(window, text="Subject:") # create "Subject:" label
		subject_lbl.grid(row=2, column=0, sticky="E", padx=10, pady=10) # place "Subject:" label

		self.subject_txt = tk.Entry(window, width=40) # create input box for subject
		self.subject_txt.grid(
			row=2, column=1, columnspan=5, sticky="W", padx=10, pady=10
		) #place input box for subject

		self.content_txt = tkst.ScrolledText(window, width=48, height=6, wrap="word") # create input box for content
		self.content_txt.grid(
			row=3, column=0, columnspan=6, sticky="W", padx=10, pady=10
		) # place input box for content

		subject_lbl = tk.Label(window, text="New priority (1-5):") # create Priority label
		subject_lbl.grid(row=4, column=0, columnspan=2, sticky="E", padx=10, pady=10) # place priority label

		self.priority_txt = tk.Entry(window, width=3) # create input box for priority
		self.priority_txt.grid(row=4, column=2, sticky="W", padx=10, pady=10) # place input box for priority

		update_btn = tk.Button(window, text="Update", command=self.update_priority) # create update button calling self.update_priority
		update_btn.grid(row=4, column=3, sticky="W", padx=10, pady=10) # place update button

		delete_btn = tk.Button(window, text="Delete", command=self.delete_message) # create delete button calling self.delete_message
		delete_btn.grid(row=4, column=4, padx=10, pady=10) # place delete button

		close_btn = tk.Button(window, text="Close", command=self.close) # create close button calling self.close
		close_btn.grid(row=4, column=5, padx=10, pady=10) # place close button

		if message_id is not None: # checking if message_id is none as a safety measure
			sender = messages.get_sender(message_id) # getting the sender from the message_id inputted
			if sender is not None: # if sender is found
				self.sender_txt.insert(tk.END, sender) # display the sender's name in the sender box
				self.sender_txt.configure(state="readonly") # setting the box to read only
				self.recipient_txt.insert(tk.END, messages.get_recipient(message_id)) #display the recipient's name in the recipient box
				self.recipient_txt.configure(state="readonly") #setting the recipient box to read only
				self.subject_txt.insert(tk.END, messages.get_subject(message_id)) # display the subject in the subject box
				self.subject_txt.configure(state="readonly") # setting the subject box to read only
				self.content_txt.insert(tk.END, messages.get_content(message_id)) # display the content of the message in the content box
			else:
				#in case the message Sender really is None, then the content section will display "No such message"
				self.content_txt.insert(tk.END, "No such message")
		# when the process is finished the content state will be set to disabled, not allowing write
		self.content_txt["state"] = "disabled"

	# declaration of the delete_message function
	def delete_message(self):
		# check if the message_id parameter is None, if not then delete the message
		if self.message_id is not None:
			messages.delete_message(self.message_id)
			# calls the close function declared below after delete
		self.close()

	# declaration of the update_priority function
	def update_priority(self):
		# check if the message_id is None, if not then get the  priority declared in the box and apply it to the message with corresponding message_id
		if self.message_id is not None:
			messages.set_priority(self.message_id, int(self.priority_txt.get()))

	# declaration of the close function
	def close(self):
		# destroy the window, meaning closing it
		self.window.destroy()


if __name__ == "__main__":  # only runs when this file is run as a standalone
	window = tk.Tk()  # create a TK object
	fonts.configure()  # configure the fonts
	ReadMessage(window, None)  # open the ReadMessage GUI
	window.mainloop()  # run the window main loop, reacting to button presses, etc
