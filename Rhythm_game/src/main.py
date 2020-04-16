"""
===========================================
Author: Codiacs
Github: github.com/MicroOptimization
===========================================
"""
import time
import tkinter as tk
from tkinter import Canvas
from ring import Ring

class Application(tk.Frame):
    
    def __init__(self, canvas, master=None):
        super().__init__(master)
        self.master = master
        self.canvas = canvas
        self.pack()
        
        self.entities = []
        
        root.update()   
        
        print("h: " , canvas.winfo_width()) #Width
        print("c: " , canvas.winfo_height()) #Height
        
        self.canvas.configure(background="#EAEBEC")
        self.canvas.pack()
        
    def update(self):
        self.canvas.delete("all")
        for object in self.entities:
            object.update()
            
    def add_entity(self, new_entity):
        self.entities.append(new_entity)
    
    def remove_entity(self, key): 
        self.entities.remove(key)
    
root = tk.Tk()

canvas = Canvas(root, width=500, height=500)
canvas.pack()


app = Application(canvas, master=root)

app.add_entity(Ring("Blue", app))


continuing_game = True
while continuing_game:
    root.update_idletasks()
    root.update()    
    time.sleep(1 / 30)
    try:
        app.update()
    except:
        print("Program terminated")
        continuing_game = False
    

    
    
    