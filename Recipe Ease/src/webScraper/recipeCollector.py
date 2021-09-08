'''
Collects recipes from api

@author: Avi J Choksi
'''

from selenium import webdriver
from pathlib import Path
import os.path

class recipeCollector(object):
    def __init__(self):
        self.urlString = ""
        self.recipes = ""
        self.names = []
        self.images = []
        self.urls = []
        self.times = []             
    
    # Create url with given filters    
    def createUrl(self, q, d, m, t):
        
        data_folder = Path(os.path.dirname(__file__))
        s = str(data_folder.parent.absolute())
        file = open(s + "//externalFiles//edamam.txt", 'r')
        codes = file.readlines()
        
        for i in range(len(d)):
            d[i] = d[i].lower()
        diet = d
        mealType = m
        time = t
        dishName = q
        dishName = dishName.replace(" ", "%20")
        
        self.urlString = "https://api.edamam.com/api/recipes/v2?type=public&q=" + dishName + "&" + codes[0] + "&" + codes[1]
        if (len(diet) > 0):
            for x in diet:
                self.urlString += "&health=" + x
        if (mealType != ""):
            self.urlString += "&mealType=" + mealType
        if (time != ""):
            self.urlString += "&time=" + time
        self.urlString += "&random=true&field=label&field=image&field=url&field=totalTime"
    
    # get recipes from api    
    def getRecipes(self):
        driver = webdriver.Chrome()
        driver.get(self.urlString)
        self.recipes = driver.find_element_by_xpath('//body//*').text
        driver.close()
        self.recipes = self.recipes.replace("{", "")
        self.recipes = self.recipes.split('[')[1]
        self.recipes = self.recipes.replace("}", "\n")
        self.recipes = self.recipes.replace("\"recipe\":", "")
        self.recipes = self.recipes.replace("\",\"", "\"\n\"")
        self.recipes = self.recipes.replace("\"label\":", "").replace("\"image\":", "").replace("\"url\":", "").replace("\"totalTime\":", "").replace(",", "").replace("]", "").replace("\"", "").replace("_links", "")
        self.recipes = self.recipes.replace(" recipes", "")
    
    # Get recipes and split into correct lists    
    def initialize(self, query, diet, mealType, time):
        self.createUrl(query, diet, mealType, time)
        self.getRecipes()
        i = 0
        for line in self.recipes.split("\n"):
            
            if line[0:4] == ":self" or line[0:5] == "title:":
                i = i + 1            
            elif i == 0:
                self.names.append(line)
                i = i + 1
            elif i == 1:
                self.images.append(line)
                i = i + 1
            elif i == 2:
                self.urls.append(line)
                i = i + 1
            elif i == 3:
                self.times.append(line)
                i = i + 1
            elif i >= 7:
                i = 0
            else:
                i = i + 1
    
    # Getters        
    def getNames(self):
        return self.names
    
    def getImages(self):
        return self.images
    
    def getTimes(self):
        return self.times
    
    def getUrls(self):
        return self.urls
