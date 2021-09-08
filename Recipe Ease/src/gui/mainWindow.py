'''
Main GUI for the recipe finder

@author: Avi J Choksi
'''

import tkinter
from tkinter import ttk
from src.gui.recipeView import recipeView
from src.user.login import login
from src.user.userInfo import userInfo

class mainWindow(object):
    # Initialize Variables
    def __init__(self):
        self.recipes = recipeView()
        self.loginPrompt = tkinter.Tk()
        self.recipeWindow = None
        self.menu = None
        self.login = login()
        self.userInfo = userInfo()
      
    # Clear recipes and load new ones    
    def refresh(self, query, diet, meal, time):
        self.recipes.delete()
        self.recipes = recipeView()
        self.recipes.createWindow(self.recipeWindow, query, diet, meal, time)
        
    # Go back to filter window
    def backToFilters(self):
            self.recipes.delete()
            self.recipes = recipeView()
            self.recipeWindow.destroy()
            self.createRecipeFilters()
    
    # Create recipe window        
    def populateRecipes(self, query, diet, meal, time):
        self.recipeWindow = tkinter.Tk()
        self.recipeWindow.minsize(900, 800)
        self.recipeWindow.title("Recipes")
        
        button_more = tkinter.Button(self.recipeWindow, command = lambda r=1: self.refresh(query, diet, meal, time), text = "More Recipes", borderwidth = 1)
        button_more2 = tkinter.Button(self.recipeWindow, command = lambda r=1: self.refresh(query, diet, meal, time), text = "More Recipes", borderwidth = 1)
        button_back = tkinter.Button(self.recipeWindow, command = lambda r=1: self.backToFilters(), text = "back", borderwidth = 1)
        
        button_more.pack(side="top")
        button_more2.pack(side="bottom")
        button_back.pack(anchor = "w", side = "bottom")
        self.recipes.createWindow(self.recipeWindow, query, diet, meal, time)
        self.recipeWindow.mainloop()
    
    # Set Filters 
    def setFilters(self, query, diet, meal, time):
        self.menu.destroy()
        chosenDiet = []
        
        # Create diet list from check box states
        for x in range(len(self.checkDiet)):
            if("selected" in diet[x]):
                chosenDiet.append(self.checkDiet[x])
        
        # Get calendar time if no time specified        
        if (time == 0 or not(time.isnumeric())):
            newTime = self.userInfo.getSecondsTillNextEvent(login)
            newTime = int(newTime/60)
            self.populateRecipes(query, chosenDiet, meal, str(newTime)) 
        # Default time (24hr)
        else:
            if not(time.isnumeric()):
                time = 86400
            self.populateRecipes(query, chosenDiet, meal, time) 
    
    # Create specification window    
    def createRecipeFilters(self):
        
        # Set labels and options
        self.menu = tkinter.Tk()
        queryLabel = ttk.Label(self.menu, text = "Query:", borderwidth = 1)
        query = ttk.Entry(self.menu)
        
        dietCheckBoxes = []
        dietLabel = ttk.Label(self.menu, text = "Diet Options:", borderwidth = 1)
        self.checkDiet = ["alcohol-free", "immuno-supportive", "celery-free", "crustacean-free", "dairy-free", "egg-free", "fish-free", "gluten-free", "keto-friendly", "kidney-friendly", "kosher", "low-potassium", "low-fat-abs", "No-oil-added", "low-sugar", "paleo", "peanut-free", "pecatarian", "pork-free", "sesame-free", "shellfish-free", "tree-nut-free", "vegan", "vegetarian"]
        
        typeLabel = ttk.Label(self.menu, text = "Mealtime:", borderwidth = 1)
        comboType = ttk.Combobox(self.menu)
        comboType['state'] = 'readonly'
        comboType['values'] = ('breakfast', 'lunch', 'dinner')
        
        timeLabel = ttk.Label(self.menu, text = "Custom Time (optional):", borderwidth = 1)
        customTime = ttk.Entry(self.menu)
        
        # Compile and send filter options
        def sendFilters():
            dietStates = []
            for x in dietCheckBoxes:
                dietStates.append(x.state())
            self.setFilters(query.get(), dietStates, comboType.get(), customTime.get())
        
        
        buttonDone = tkinter.Button(self.menu, command = lambda r=1: sendFilters(), text = "Done", borderwidth = 1)
        
        buttonDone.pack(side="bottom")
        queryLabel.pack(side="top")
        query.pack(side="top")
        dietLabel.pack(side="top")
        
        # Create check boxes for diet
        for x in range(len(self.checkDiet)):
            l = ttk.Checkbutton(self.menu, text = self.checkDiet[x], variable = self.checkDiet[x])
            l.state(['!alternate'])
            l.pack(side="top")
            dietCheckBoxes.append(l)
            
        typeLabel.pack(side="top")
        comboType.pack(side="top")
        timeLabel.pack(side="top")
        customTime.pack(side="top")
        self.menu.mainloop()
        
            
    # Login user and create filter window    
    def loginUser(self):
        self.login.login()
        self.loginPrompt.destroy()
        self.createRecipeFilters() 
    
    # Create login window    
    def loginWindow(self):
        buttonLogin = tkinter.Button(self.loginPrompt, command = lambda r=1: self.loginUser(), text = "Login", borderwidth = 1)
        buttonLogin.pack(side="top")
        self.loginPrompt.mainloop()
        
a = mainWindow()
a.loginWindow()