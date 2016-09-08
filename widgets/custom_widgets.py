import tkinter as tk

class ctkButton(tk.Button):

	def __init__(self, parent, text, command):
		tk.Button.__init__(self, text=text, command=command)
		self.pack()