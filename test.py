import tkinter as tk
from PIL import Image, ImageTk

class RYBapp(tk.Tk):

	def __init__(self):

		tk.Tk.__init__(self)
		container = tk.Frame(self)

		container.pack(side="top", fill="both", expand = True)

		self.frames = {}

		for F in (StartPage, PageOne):
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

		button1 = tk.Button(self, text="Page 1", 
			command=lambda: controller.show_frame(PageOne))
		button1.pack()


class PageOne(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="I'm on the second page!!")
		label.pack()

		button1 = tk.Button(self, text="Home", 
			command=lambda: controller.show_frame(StartPage))
		button1.pack()



app = RYBapp()
app.mainloop()