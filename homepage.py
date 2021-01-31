import tkinter as tk
from tkinter import ttk,filedialog
import page as p
import json
import csv

class HomePage(p.Page):
    def __init__(self, *args, **kwargs):
        p.Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text = "Food Page") 
        label.pack(side="top", fill="both")

        self.tble = ttk.Treeview(self, columns=(1,2),show ="headings", height=15) 
        self.tble.pack(side="top")

        self.tble.heading(1, text = "Food")
        self.tble.heading(2, text = "Calories")

        self.b4 = tk.Button(self, text="Export", width=10, command= lambda: self.writetoFile(p.foods))
        self.b5 = tk.Button(self, text="Import", width=10, command= lambda: self.importfromFile(p.foods))
        self.b6 = tk.Button(self, text="Delete", width=10, command=self.delItem)
        self.b4.pack()
        self.b4.place(x=70,y=380)
        self.b5.pack()
        self.b5.place(x=225,y=380)
        self.b6.pack()
        self.b6.place(x=375,y=380)

    def show(self):
        p.Page.show(self)
        self.update()

    def update(self):
        index = iid = 0
        self.tble.delete(*self.tble.get_children())
        for row in p.foods:
            self.tble.insert("", index, iid, values=row)
            index = iid = index + 1

    def delItem(self):
        select = int(self.tble.focus())
        self.tble.delete(select)
        del p.foods[select]
        self.update()

    def writetoFile(self,foodList):
        with open("cache.csv", "w", newline='') as f:
            w=csv.writer(f, delimiter=',')
            for i in foodList:
                w.writerow(i)

        newWindow = tk.Toplevel(self) 
        newWindow.title("Export Complete") 
        newWindow.geometry("200x50") 
        tk.Label(newWindow,  text ="Export Complete").pack() 
        tk.Button(newWindow, text = "Close", command = newWindow.destroy).pack()
        
    
    def importfromFile(self,foodList):
        filen = filedialog.askopenfilename(title = "Select file",filetypes = (("CSV Files","*.csv"),))
        with open(filen) as f:
            w= csv.reader(f,delimiter=',')
            foodList.clear()
            for i in w:
                foodList.append(i)
        self.update()