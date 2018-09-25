# 2 textfelder und ein Button
from tkinter import *

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.textOne = Entry(frame)
        self.textOne.pack(side=LEFT)
        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)
        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        s = self.textOne.get()
        print ("hi there, everyone!")
        print (s)

root = Tk()
app = App(root)

root.mainloop()
root.destroy() # optional; see description below