from tkinter import *
import sys

Root=Tk()
RTitle=Root.title("Windows")
RWidth=Root.winfo_screenwidth()
RHeight=Root.winfo_screenheight()
Root.geometry(("%dx%d")%(RWidth,RHeight))

mainloop()