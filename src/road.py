import pygame as pg

class Road:

    x = 0.0
    y = 0.0
    width = 0.0
    height = 0.0
    DISPLAY = 0.0

    def __init__(self, x, y, width, height, DISPLAY):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.DISPLAY = DISPLAY

    def draw(self):
        pg.draw.rect(self.DISPLAY, (128, 128, 128), (self.x, self.y, self.width, self.height/4.0))



