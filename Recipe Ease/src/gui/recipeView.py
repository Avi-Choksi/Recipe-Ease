'''
Window for listing recipes

@author: Avi J Choksi
'''

import tkinter 
from PIL import ImageTk, Image
import io
import urllib.request
import webbrowser
from src.webScraper.recipeCollector import recipeCollector


class recipeView(object):
    
    def __init__(self):
        self.names = []
        self.imageUrls = []
        self.images = []
        self.times = []
        self.urlLinks = []       
        self.recipes = recipeCollector()
        self.canvas = None
        self.vsb = None
    
    # Get all recipe info
    def getRecipes(self, query, diet, meal, time):
        self.recipes.initialize(query, diet, meal, "1-" + time)
        self.names = self.recipes.getNames()
        self.imageUrls = self.recipes.getImages()
        self.times = self.recipes.getTimes()
        self.urlLinks = self.recipes.getUrls()
    
    # Populate window
    def populate(self, frame):
        '''Populate with data'''
        for r in range(len(self.names)):
            
            # Set images
            if (r < len(self.imageUrls) and self.imageUrls[r] != "" and self.imageUrls[r] != " "):
                try:
                    raw_data = urllib.request.urlopen(self.imageUrls[r]).read()
                    im = Image.open(io.BytesIO(raw_data))
                    image = ImageTk.PhotoImage(im)
                    tkinter.Label(frame, image = image, borderwidth = 1).grid(row = r, column = 0)
                    self.images.append(image)
                except:
                    None
            
            # Set recipe names        
            tkinter.Label(frame, text = self.names[r], borderwidth = 1).grid(row = r, column = 1)
            
            # Set recipe url
            tkinter.Button(frame, command = lambda r=r: webbrowser.open_new(self.urlLinks[r]), text = "Click For Recipe", borderwidth = 1).grid(row = r, column = 2)
            
            # Set recipe time
            if (r < len(self.times) and self.times[r] != "" and self.times[r] != " "):
                tkinter.Label(frame, text = self.times[r] + " Minutes", borderwidth = 1).grid(row = r, column = 3)           
        frame.grid_columnconfigure(3, minsize=100)
    
    def onFrameConfigure(self, canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))
    
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    # Create the window
    def createWindow(self, root, query, diet, meal, time):
        self.getRecipes(query, diet, meal, time)
        # root = tkinter.Tk()
        # root.title("Recipes")
        self.canvas = tkinter.Canvas(root, borderwidth=0, background="#ffffff")
        frame = tkinter.Frame(self.canvas, background="#ffffff")
        self.vsb = tkinter.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=frame, anchor="nw")
        
        frame.bind("<Configure>", lambda event, canvas=self.canvas: self.onFrameConfigure(canvas))
        
        self.populate(frame)
    
        root.mainloop()
    
    # Delete window    
    def delete(self):
        self.canvas.pack_forget()
        self.vsb.pack_forget()
        self.canvas.destroy()
        self.vsb.destroy()
    
