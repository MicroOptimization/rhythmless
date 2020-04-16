"""
===========================================
Author: Codiacs
Github: github.com/MicroOptimization
===========================================
"""
import time
import tkinter as tk
from tkinter import Canvas

class Application(tk.Frame):
    
    def __init__(self, canvas, master=None):
        super().__init__(master)
        self.master = master
        self.canvas = canvas
        self.pack()
        
        self.entities = []
    
    def update(self):
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




continuing_game = True
while continuing_game:
    root.update_idletasks()
    root.update()
    time.sleep(0.2)
    app.update()
