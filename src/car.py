import pygame as pg

class Car:

    x = 0.0
    y = 0.0
    width = 0.0
    height = 0.0
    speed = 0.0
    lights_off = 180
    lights_on = 180
    DISPLAY = 0
    prevSpeed = 0.0

    def __init__(self, x, y, speed, DISPLAY):
        self.x = x
        self.y = y
        self.width = 1080 * 7 / 100
        self.height = self.width / 1.5
        self.speed = speed
        self.lights_off = 180
        self.lights_on = 180
        self.DISPLAY = DISPLAY

    def draw(self):
        pg.draw.rect(self.DISPLAY, (50, 50, 200), (self.x, self.y, self.width, self.height))
        pg.draw.rect(self.DISPLAY, (0, 0, 0), (self.x, self.y, self.width, self.height), 2)
        pg.draw.rect(self.DISPLAY, (0, 0, 0), (self.x+self.width/4, self.y+(self.height/4), self.width/2, self.height/2))

        pg.draw.rect(self.DISPLAY, (150, 150, 200), (self.x+self.width/4 - 5, self.y+(self.height/4), self.width/1.5, self.height/2))

        pg.draw.rect(self.DISPLAY, (180, 180, 180), (self.x+self.width/4, self.y+(self.height/4), self.width/2, self.height/2))

        pg.draw.rect(self.DISPLAY, (255, 255, 255), (self.x+self.width/4, self.y+(self.height/4), self.width/2, self.height/2), 1)

        pg.draw.rect(self.DISPLAY, (100, 100, 100), (self.x+self.width-self.width/8, self.y+(self.height/8), self.width/8, self.height*6/8))
        pg.draw.circle(self.DISPLAY, (self.lights_on, self.lights_off, self.lights_off), (int(self.x + 9), int(self.y + self.height - 9)), 8)
        pg.draw.circle(self.DISPLAY, (self.lights_on, self.lights_off, self.lights_off), (int(self.x + 9), int(self.y + 9)), 8)

    def move(self, speed):
        self.x += 1.0 * speed

        if speed >= self.prevSpeed or self.x >= 1080*85/100:
            self.lights_off = 100
            self.lights_on = 100
        else:
            self.lights_off = 0
            self.lights_on = 255

        self.prevSpeed = speed
        if self.x > 1080:
            self.x = 0


