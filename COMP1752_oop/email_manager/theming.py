import tkinter as tk

# Define themes
MOCHA = {
	"base": "#1e1e2e",
	"text": "#cdd6f4",
	"mantle": "#181825",
	"blue": "#89b4fa",
	"surface0": "#313244",
}

DEFAULT_THEME = {
	"base": "#d9d9d9",
	"text": "#000000",
	"mantle": "#ffffff",
	"blue": "#d9d9d9",
	"surface0": "#d9d9d9",
}

# Track current theme state
is_dark_theme = False

def apply_theme_palette(root, palette):
	# Applies a color palette dictionary to the option database.
	root.configure(bg=palette["base"])

	root.option_add("*Background", palette["base"])
	root.option_add("*Foreground", palette["text"])

	root.option_add("*Entry.background", palette["mantle"])
	root.option_add("*Entry.foreground", palette["text"])
	root.option_add("*Entry.insertBackground", palette["text"])

	root.option_add("*Text.background", palette["mantle"])
	root.option_add("*Text.foreground", palette["text"])
	root.option_add("*Text.insertBackground", palette["text"])

	root.option_add("*Button.background", palette["blue"])
	root.option_add("*Button.foreground", palette["base"] if palette == MOCHA else palette["text"])
	root.option_add("*Button.activeBackground", palette["surface0"])

	# Update existing widgets in real time
	update_widget_colors(root, palette)

def update_widget_colors(widget, palette):
	# Recursively updates colors on existing widgets without throwing option errors.
	for child in widget.winfo_children():
		widget_type = child.winfo_class()

		if widget_type in ("Frame", "TLabelframe", "Toplevel"):
			child.configure(bg=palette["base"])

		# Labels and Checkbuttons accept both bg and fg
		elif widget_type in ("Label", "Checkbutton", "Radiobutton"):
			child.configure(bg=palette["base"], fg=palette["text"])

		# Text fields & Entries accept bg, fg, and cursor color
		elif widget_type in ("Entry", "Text"):
			child.configure(
				bg=palette["mantle"],
				fg=palette["text"],
				insertbackground=palette["text"]
			)

		# Buttons accept bg and fg
		elif widget_type == "Button":
			child.configure(
				bg=palette["blue"],
				fg=palette["base"] if palette == MOCHA else palette["text"],
				activebackground=palette["surface0"]
			)

		# Recursively process nested containers
		update_widget_colors(child, palette)

def toggle_theme(root):
	# Toggles between Catppuccin Mocha and default styling.
	global is_dark_theme
	is_dark_theme = not is_dark_theme

	if is_dark_theme:
		apply_theme_palette(root, MOCHA)
	else:
		apply_theme_palette(root, DEFAULT_THEME)
