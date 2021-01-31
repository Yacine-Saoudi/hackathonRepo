import tkinter as tk
import requests
import requests
import json
# from tkinter import ttk
# from ttkthemes import themed_tk as themedtk

# name = input()
# name = name.replace(" ", "%")

# print(name)

# url = "https://nutritionix-api.p.rapidapi.com/v1_1/search/"+name

# querystring = {"fields":"item_name,item_id,brand_name,nf_calories,nf_total_fat"}

# headers = {
#     'x-rapidapi-key': "9ee4c686aamsh3bf6533ecf5a513p118bcejsn7facbf98286b",
#     'x-rapidapi-host': "nutritionix-api.p.rapidapi.com"
#     }

# response = requests.request("GET", url, headers=headers, params=querystring)

# data=response.json()
# str=data['hits'][0]['fields']['item_name']
# qty = str.split("-")

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        print("showing")
        self.lift()

class HomePage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text = "Food Page") 
        label.pack(side="top", fill="both", expand=True)
        self.listbox = tk.Listbox(self)
        self.listbox.pack()

    def update(self, foodList):
        self.listbox.delete(0, tk.END)
        for food in foodList:
            self.listbox.insert(tk.END, food)
        self.listbox.pack(side="top", expand=True)

class SearchPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text = "Search Page") 
        label.pack(side="top", fill="both", expand=True)
        
class CalcPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text = "Calc Page") 
        label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        home = HomePage(self)
        search = SearchPage(self)
        calc = CalcPage(self)

        buttonFrame = tk.Frame(self, height=600, width=50, bg="blue")
        container = tk.Frame(self, height=600, width=750, bg="yellow")
        buttonFrame.pack(side="left", fill="y", expand=False)
        container.pack(side="right", fill="both", expand=True)

        home.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        search.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        calc.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonFrame, width=8, height=5, text="Home", command=home.show)
        b2 = tk.Button(buttonFrame, width=8, height=5, text="Search", command=search.show)
        b3 = tk.Button(buttonFrame, width=8, height=5, text="Calculator", command=calc.show)
        b1.pack(side="top")
        b2.pack(side="top")
        b3.pack(side="top")

        foodList = ["apple", "banana", "cheese"]
        home.update(foodList)

        home.show()  


if __name__ == "__main__":
    #root = tk.Themedtk()
    master = tk.Tk()
    # master.get_themes()
    # master.set_theme("PLastik")

    main = MainView(master, bg="green")
    main.pack(side="top", fill="both", expand="True")
    master.wm_geometry("800x600")

    master.mainloop()




