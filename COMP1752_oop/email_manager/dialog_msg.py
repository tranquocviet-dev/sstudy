import tkinter as tk
def dialog(title, message, window):
	# Create a top-level window instead of messagebox
	dialog = tk.Toplevel(window)
	dialog.title(title)
	dialog.geometry("300x120")
	dialog.resizable(False, False)
	
	# Keep dialog on top
	dialog.transient(window)
	dialog.attributes("-topmost", True)
	
	label = tk.Label(dialog, text=message, wraplength=260, pady=15)
	label.pack()
	
	btn = tk.Button(dialog, text="OK", width=10, command=dialog.destroy)
	btn.pack()
	
	# Force focus on Wayland
	dialog.focus_force()
