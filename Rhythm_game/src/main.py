"""
===========================================
Author: Codiacs
Github: github.com/MicroOptimization
===========================================
"""
import time
import tkinter as tk
from tkinter import Canvas, W
from ring import Ring

class Application(tk.Frame):
    
    def __init__(self, canvas, master=None):
        super().__init__(master)
        self.master = master
        self.canvas = canvas
        self.pack()
        
        self.entities = []
        
        
                
        self.canvas.configure(background="#EAEBEC")
        self.canvas.pack()
        
    def draw_target(self):
        root.update()
        final_radius = 69
        self.ring_x0 = (self.canvas.winfo_width() - final_radius) / 2
        self.ring_y0 = (self.canvas.winfo_height() - final_radius) - 4
        self.ring_x1 = (self.canvas.winfo_width() + final_radius) / 2
        self.ring_y1 = (self.canvas.winfo_height()) - 4
        
        self.canvas.create_oval(self.ring_x0, self.ring_y0, 
                                self.ring_x1, self.ring_y1)
        #Give or take should be this: 218.5 433 285.5 500
        #Old Ver: self.canvas.create_oval(220, 440, 280, 500)
        
        self.hit_msg = ""
        
        self.canvas.bind("<Key>", self.key_listener)
        self.canvas.bind("<Button-1>", self.focuser)
        
    def key_listener(self, event):
        key = repr(event.char) 
        if key == "'q'":
            self.entities.append(Ring("blue", self))
        else:
            for i in self.entities:
                if type(i) is Ring:
                    ring = i
                    print("Ring pos: " , ring.y)
                    self.check_accuracy(ring.y)
               
    def check_accuracy(self, y):
        if y >= 480:
            print("Miss")
            msg = "Miss"
        
        elif y >= 455:
            print("Okay")
            msg = "Okay"

        elif y >= 430:
            print("Great")
            msg = "Great"

        elif y >= 420:
            print("Excellent")
            msg = "Excellent"
        elif y <= 420:
            print("Great")
            msg = "Great"
            
        elif y <= 410:
            print("You missed")
            msg = "Miss"
            
    def focuser(self, event):
        self.canvas.focus_set()
        
    def update(self):
        self.canvas.delete("all")
        
        for object in self.entities:
            object.update()
        self.draw_target()
    
    def add_entity(self, new_entity):
        self.entities.append(new_entity)
    
    def remove_entity(self, key): 
        self.entities.remove(key)
    
root = tk.Tk()

canvas = Canvas(root, width=500, height=500)
canvas.pack()


app = Application(canvas, master=root)

#app.add_entity(Ring("Blue", app))
app.add_entity(Ring("#264348", app))
#264348

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
    

    
    
    