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
        self.diameter = 20
        self.y_pos = 0
        
    def draw(self):
        print("drawing")
        