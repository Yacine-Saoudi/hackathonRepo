import tkinter as tk
from homepage import *
from searchpage import *
from calcpage import *

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        home = HomePage(self)
        search = SearchPage(self)
        calc = CalcPage(self)

        buttonFrame = tk.Frame(self, height=600, width=50, highlightbackground="black", highlightthickness=1, bg="sky blue")
        container = tk.Frame(self, height=600, width=750)
        buttonFrame.pack(side="left", fill="y", expand=False)
        container.pack(side="right", fill="both", expand=True)

        home.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        search.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        calc.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonFrame, width=8, height=5, text="Home", bg="medium aquamarine", command=home.show)
        b2 = tk.Button(buttonFrame, width=8, height=5, text="Search", bg="deep sky blue", command=search.show)
        b3 = tk.Button(buttonFrame, width=8, height=5, text="Calculator", bg="royal blue", command=calc.show)
       
        b1.pack(side="top")
        b2.pack(side="top")
        b3.pack(side="top")
        
        home.update()

        home.show()  

if __name__ == "__main__":
    master = tk.Tk()

    main = MainView(master)
    main.pack(side="top", fill="both", expand="True")
    master.wm_geometry("600x450")
    master.resizable(0, 0) 
    master.mainloop()
