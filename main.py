import tkinter as tk
from tkinter import ttk,filedialog
import requests
import json
import csv

foods = []

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class HomePage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text = "Food Page") 
        label.pack(side="top", fill="both")

        self.tble = ttk.Treeview(self, columns=(1,2),show ="headings", height=15) 
        self.tble.pack(side="top")

        self.tble.heading(1, text = "Food")
        self.tble.heading(2, text = "Calories")

        self.b4 = tk.Button(self, text="Export", width=10, command= lambda: self.writetoFile(foods))
        self.b5 = tk.Button(self, text="Import", width=10, command= lambda: self.importfromFile(foods))
        self.b6 = tk.Button(self, text="Delete", width=10, command=self.delItem)
        self.b4.pack()
        self.b4.place(x=70,y=380)
        self.b5.pack()
        self.b5.place(x=225,y=380)
        self.b6.pack()
        self.b6.place(x=375,y=380)

    def show(self):
        Page.show(self)
        self.update()

    def update(self):
        index = iid = 0
        self.tble.delete(*self.tble.get_children())
        for row in foods:
            self.tble.insert("", index, iid, values=row)
            index = iid = index + 1

    def delItem(self):
        select = int(self.tble.focus())
        self.tble.delete(select)
        del foods[select]
        self.update()

    def writetoFile(self,foodList):
        with open("cache.csv", "w", newline='') as f:
            w=csv.writer(f, delimiter=',')
            for i in foodList:
                w.writerow(i)

        newWindow = tk.Toplevel(master) 
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

class SearchPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text = "Search Page") 
        label.pack(side="top", fill="both")
        
        self.searchF = tk.Entry(self, width=50)
        self.searchF.insert(0, "Search for a food...")
        self.searchF.pack(side="top")

        searchB = tk.Button(self, text="SEARCH", command=self.resultUpdate)
        searchB.pack(side="top")

        self.listbox = tk.Listbox(self, width=70, height=20)
        self.listbox.pack(side="top")

        addB = tk.Button(self, text="Add", command=self.addItem)
        addB.pack(side="top")

    def resultUpdate(self):
        name = self.searchF.get().replace(" ", "%")
        url = "https://nutritionix-api.p.rapidapi.com/v1_1/search/"

        querystring = {"fields":"item_name,item_id,brand_name,nf_calories,nf_total_fat"}

        headers = {
            'x-rapidapi-key': "9ee4c686aamsh3bf6533ecf5a513p118bcejsn7facbf98286b",
            'x-rapidapi-host': "nutritionix-api.p.rapidapi.com"
            }

        response = requests.request("GET", url+name, headers=headers, params=querystring)
        data=response.json()
        self.searchList = data['hits']
        
        self.listbox.delete(0, tk.END)
        if self.searchList == []:
            self.listbox.insert(tk.END, "NO RESULTS FOUND")

        for i in range(len(self.searchList)):
                entry = self.searchList[i]['fields']['item_name'] + "    Calories: " + str(self.searchList[i]['fields']['nf_calories'])
                self.listbox.insert(tk.END, entry)

        self.listbox.pack(side="top")
        
    def addItem(self):
        select = self.listbox.curselection()[0]
        foodItem=[]
        foodItem.append(self.searchList[select]['fields']['item_name'])
        foodItem.append(self.searchList[select]['fields']['nf_calories'])
        foods.append(foodItem)
        print(foods)

class CalcPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.labelTotal = tk.Label(self, text ="Calories: 0") 
        self.labelTotal.pack(side="top", fill="both")
        
        self.labelGoal = tk.Label(self, text = "No current Goal!") 
        self.labelGoal.pack(side="top", fill="both")

        self.goalF = tk.Entry(self)
        self.goalF.insert(0, "Enter Goal Daily Calories")
        self.goalF.pack(side="top")
        
        goalB = tk.Button(self, text="ENTER", command=self.update)
        goalB.pack(side="top")

    def show(self):
        Page.show(self)
        self.update()

    def update(self):
        total=0
        for food in foods:
            total+=food[1]
        
        self.labelTotal.config(text="Calories: "+ str(total))

        goal=self.goalF.get()
        goal=int(goal)
        if (goal>total):
            self.labelGoal.config(text="You are "+str(abs(goal-total))+" Calories below your goal!")
        elif (goal==total):
            self.labelGoal.config(text="You are at your goal!")
        else:
            self.labelGoal.config(text="You are "+str(abs(goal-total))+" Calories above your goal!")

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
