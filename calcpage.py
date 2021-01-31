import tkinter as tk
import page as p

class CalcPage(p.Page):
    def __init__(self, *args, **kwargs):
        p.Page.__init__(self, *args, **kwargs)
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
        p.Page.show(self)
        self.update()

    def update(self):
        total=0
        for food in p.foods:
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
