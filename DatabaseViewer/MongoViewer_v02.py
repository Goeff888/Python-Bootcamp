import pymongo
from pymongo import MongoClient
import tkinter as tk
from tkinter import Tk, BOTH, Menu

def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print ('You selected item %d:' ,index, value)
    #Hier Anzeige von Eintr?gen in Collection

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.showCons = tk.Menubutton(self,text="condiments")
        self.showCons.grid()
        self.showCons.menu =  Menu(self.showCons, tearoff = 0 )#menu wird nicht erkannt
        self.showCons["menu"] =  self.showCons.menu

        mayoVar  = tk.IntVar()
        ketchVar = tk.IntVar()

        self.showCons.menu.add_checkbutton ( label="mayo",variable=mayoVar )
        self.showCons.menu.add_checkbutton ( label="ketchup",variable=ketchVar )
        self.showCons.pack()
        
        self.createCon = tk.Button(self,command=self.createCon)
        self.createCon["text"] = "Verbindung aufbauen"
        #self.createCon["command"] = self.createCon
        self.createCon.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.quit.pack(side="bottom")

        
    def createCon(self):
        print("Verbindung aufbauen")
        client = MongoClient("localhost", 27017)
        dbHomepage = client["homepage"]
        colHomepage = dbHomepage.list_collection_names()
        print(dbHomepage.list_collection_names())
        self.lbCollections = tk.Listbox(self)
        self.lbCollections.pack()
        self.lbCollections.bind('<<ListboxSelect>>', onselect)
        for item in colHomepage:
            self.lbCollections.insert(tk.END,item)
      

root = tk.Tk()
RTitle=root.title("Windows")
RWidth=root.winfo_screenwidth()/2
RHeight=root.winfo_screenheight()/2
root.geometry(("%dx%d")%(RWidth,RHeight))
app = Application(master=root)
app.mainloop()