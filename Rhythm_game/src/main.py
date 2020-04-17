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
        
        self.final_radius = 69
        
        self.canvas.bind("<Key>", self.key_listener)
        self.canvas.bind("<Button-1>", self.focuser)
        
        self.canvas.configure(background="#EAEBEC")
        self.canvas.pack()
        
        self.create_bounds()
        self.update()
        
    def draw_target(self):
        root.update()
        
        self.ring_x0 = (self.canvas.winfo_width() - self.final_radius) / 2
        self.ring_y0 = (self.canvas.winfo_height() - self.final_radius) - 54 
        self.ring_x1 = (self.canvas.winfo_width() + self.final_radius) / 2
        self.ring_y1 = (self.canvas.winfo_height()) - 54
        
        self.canvas.create_oval(self.ring_x0, self.ring_y0, 
                                self.ring_x1, self.ring_y1)
        #Give or take should be this: 218.5 433 285.5 500
        #Old Ver: self.canvas.create_oval(220, 440, 280, 500)
        
        self.hit_msg = ""
        
    def key_listener(self, event):
        key = repr(event.char) 
        if key == "'q'":
            self.entities.append(Ring("blue", self))
        else:
            for i in self.entities:
                if type(i) is Ring:
                    ring = i
                    print("Ring pos: " , ring.y)
                    msg = self.check_accuracy(ring.y)

    def create_bounds(self):
        #Setting bounds for target rings
        
        self.tightest_ub = (self.canvas.winfo_height() / 2)
        self.tightest_lb = ((self.canvas.winfo_height() - self.final_radius) / 2)
        
        self.e_ub = self.tightest_ub
        self.e_lb = self.tightest_lb
        
        self.g_ub = self.tightest_ub + 10
        self.g_lb = self.tightest_lb - 10
        
        self.o_ub = self.tightest_ub + 20
        self.o_lb = self.tightest_lb - 20
        
        self.m_ub = self.tightest_lb + 50
        self.m_lb = self.tightest_lb - 50
    

    def create_bound_debug_lines(self):
        canvas.create_line(0, self.e_ub, canvas.winfo_width(), self.e_ub, fill="blue", width=2)
        canvas.create_line(0, self.e_lb, canvas.winfo_width(), self.e_lb, fill="blue", width=2)
        
        canvas.create_line(0, self.g_ub, canvas.winfo_width(), self.g_ub, fill="red", width=2)
        canvas.create_line(0, self.g_lb, canvas.winfo_width(), self.g_lb, fill="red", width=2)
        
        canvas.create_line(0, self.o_ub, canvas.winfo_width(), self.o_ub, fill="green", width=2)
        canvas.create_line(0, self.o_lb, canvas.winfo_width(), self.o_lb, fill="green", width=2)
        
        canvas.create_line(0, self.m_ub, canvas.winfo_width(), self.m_ub, fill="black", width=2)
        canvas.create_line(0, self.m_lb, canvas.winfo_width(), self.m_lb, fill="black", width=2)
        
        
    def check_accuracy(self, y):
        msg = ""
        
        print("y: " , y)
        print()
        print(self.e_lb, self.e_ub)
        print(self.g_lb, self.g_ub)
        print(self.o_lb, self.o_ub)
        print(self.m_lb, self.m_ub)
        
        
        if y <= self.e_ub and y >= self.e_lb:
            print("Excellent")
            msg = "Excellent"
        elif y <= self.g_ub and y >= self.g_lb:
            print("Great")
            msg = "Great"

        elif y >= self.o_ub and y <= self.o_lb:
            print("Okay")
            msg = "Okay"
        else:
            print("You missed")
            msg = "Miss"

        return msg
        
    def focuser(self, event):
        self.canvas.focus_set()
        
    def update(self):
        self.canvas.delete("all")
        
        for object in self.entities:
            object.update()
        self.draw_target()
        self.create_bound_debug_lines()
        
    def add_entity(self, new_entity):
        self.entities.append(new_entity)
    
    def remove_entity(self, key): 
        self.entities.remove(key)
    
root = tk.Tk()

canvas = Canvas(root, width=500, height=500)
canvas.pack()

canvas.create_text(100, 100, anchor=W, font="Purisa",
                text="{}".format("asd"))
        

app = Application(canvas, master=root)

app.add_entity(Ring("#264348", app))

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
    

    
    
    