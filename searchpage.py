import tkinter as tk
import requests
import page as p

class SearchPage(p.Page):
    def __init__(self, *args, **kwargs):
        p.Page.__init__(self, *args, **kwargs)
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
        p.foods.append(foodItem)
        print(p.foods)
