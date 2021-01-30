from tkinter import *
master = Tk()
master.geometry("600x400")
master.resizable(0, 0)

x = "YO YO YO YO YO"
print(x)
TitleText = Button(master, text=x, bd=0, font="Verdana 19 bold")
TitleText.pack()
TitleText.place(x=160, y=15)
mainloop()
