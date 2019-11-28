import pygame as pg

class TrafficLight:

    x = 0
    y = 0
    red_col = 3000.0
    green_col = 3000.0
    orange_col = 1500.0
    state = 0.0
    DISPLAY = 0.0

    def __init__(self, x, y, DISPLAY):
        self.x = int(x)
        self.y = int(y)
        self.state = 1
        self.stage = 2
        self.DISPLAY = DISPLAY
        self.tlDistance = ""
        self.tlColor = ""

    def draw(self):
        pg.draw.rect(self.DISPLAY, (0, 0, 0), (self.x-1-10, self.y-1-10, 22, 62))

        if self.stage == 2:
            pg.draw.circle(self.DISPLAY, (255, 0, 0), (self.x, self.y), 10)
        else:
            pg.draw.circle(self.DISPLAY, (180, 180, 180), (self.x, self.y), 10)

        if self.stage == 1:
            pg.draw.circle(self.DISPLAY, (255, 255, 0), (self.x, self.y+20), 10)
        else:
            pg.draw.circle(self.DISPLAY, (180, 180, 180), (self.x, self.y+20), 10)

        if self.stage == 0:
            pg.draw.circle(self.DISPLAY, (0, 255, 0), (self.x, self.y+40), 10)
        else:
            pg.draw.circle(self.DISPLAY, (180, 180, 180), (self.x, self.y+40), 10)

    def update(self):
        self.state += 1

        if self.state == self.red_col:
            self.stage = 0
        else:
            if self.state == (self.red_col + self.green_col):
                self.stage = 1
            else:
                if self.state == self.red_col+self.green_col+self.orange_col:
                    self.state=1
                    self.stage=2

