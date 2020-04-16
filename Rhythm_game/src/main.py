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
        
        root.update()   
        
        print("h: " , canvas.winfo_width()) #Width
        print("c: " , canvas.winfo_height()) #Height
        
        self.canvas.configure(background="#EAEBEC")
        self.canvas.pack()
        
    def draw_target(self):
        root.update()
        final_radius = 67
        self.ring_x0 = (self.canvas.winfo_width() - final_radius) / 2
        self.ring_y0 = (self.canvas.winfo_height() - final_radius) - 4
        self.ring_x1 = (self.canvas.winfo_width() + final_radius) / 2
        self.ring_y1 = (self.canvas.winfo_height()) - 4
        
        self.canvas.create_oval(self.ring_x0, self.ring_y0, 
                                self.ring_x1, self.ring_y1)
        #Give or take should be this: 218.5 433 285.5 500
        #Old Ver: self.canvas.create_oval(220, 440, 280, 500)
        
        self.hit_msg = ""
        
    """
    def update_hit_msg(self, msg):
        self.hit_msg = msg
    
    def send_hit_msg(self, msg):
        self.hit_msg = msg
        print("hm: " , msg)    
        self.canvas.create_text(50, 50, anchor=W, font="Purisa",
                text="{}".format(self.hit_msg))
    """    
        
    def update(self):
        self.canvas.delete("all")
        
        self.draw_target()
        for object in self.entities:
            object.update()
        #print("Message: " , self.hit_msg)
        #self.send_hit_msg(self.hit_msg)
        
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
    time.sleep(1 / 120)
    try:
        app.update()
    except:
        print("Program terminated")
        continuing_game = False
    

    
    
    