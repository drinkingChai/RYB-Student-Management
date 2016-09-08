import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

#custom module import
import sys
sys.path.insert(0, './widgets')
import custom_widgets as cwd
#======================================#

def popupmsg(msg):
	popup = tk.Tk()
	popup.wm_title("!")
	label = ttk.Label(popup, text=msg)
	label.pack(side="top", fill="x", pady=10)
	B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
	B1.pack()
	popup.mainloop()


class RYBapp(tk.Tk):

	def __init__(self):

		tk.Tk.__init__(self)
		tk.Tk.iconbitmap(self, default="app_icon.ico")

		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand = True)

		menubar = tk.Menu(container)
		filemenu = tk.Menu(menubar, tearoff=0)
		filemenu.add_command(label="Save settings", command=lambda: popupmsg("Not yet!"))
		filemenu.add_separator()
		menubar.add_cascade(label="File", menu = filemenu)
		tk.Tk.config(self, menu=menubar)

		self.frames = {}

		for F in (StartPage, PageOne, PageTwo):
			frame = F(container, self)

			self.frames[F] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)


	def show_frame(self, cont):

		frame = self.frames[cont]
		frame.tkraise()


class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="whatever!")
		label.pack()

		button1 = cwd.ctkButton(self, text="Page 1", 
			command=lambda: controller.show_frame(PageOne))
		button2 = ttk.Button(self, text="Page 2", 
			command=lambda: controller.show_frame(PageTwo))
		#button1.pack()
		button2.pack()


class PageOne(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="I'm on the second page!!")
		label.pack()

		button1 = ttk.Button(self, text="Home", 
			command=lambda: controller.show_frame(StartPage))
		button2 = ttk.Button(self, text="Page 2", 
			command=lambda: controller.show_frame(PageTwo))
		button1.pack()
		button2.pack()


class PageTwo(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="I'm on the third page :o")
		label.pack()

		button1 = ttk.Button(self, text="Home", 
			command=lambda: controller.show_frame(StartPage))
		button2 = ttk.Button(self, text="Page 1", 
			command=lambda: controller.show_frame(PageOne))
		button1.pack()
		button2.pack()


app = RYBapp()
app.mainloop()