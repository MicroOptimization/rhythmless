"""
===========================================
Author: Codiacs
Github: github.com/MicroOptimization
===========================================
"""

class Ring():
    
    def __init__(self, colour, app):
        self.colour = colour
        self.app = app
        self.canvas = app.canvas
        self.diameter = 20
        self.y_pos = 0
    
    def update(self):
        self.draw()
    
    def draw(self):
        self.canvas.create_oval(10, 10, 50, 50)