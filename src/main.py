import pygame, sys
from pygame.locals import *
from car import Car
from TrafficLight import TrafficLight
from road import Road
import skfuzzy as fuzz


def trimf(x, a, b, c):
    if x <= a or c <= x:
        return 0
    elif a <= x and x <= b:
        return (x - a) / (b - a)
    elif b <= x and x <= c:
        return (c - x) / (c - b)


def fuzzy_logic(tl_state, tl_position, car_position):
    if car_position < tl_position/3:
        traffic_light.tlDistance = "far"
    elif car_position > tl_position * 2/3:
        traffic_light.tlDistance = "close"
    else:
        traffic_light.tlDistance = "middle"

    if tl_state < traffic_light.red_col:
        traffic_light.tlColor = "Red"
    elif tl_state > traffic_light.red_col+traffic_light.green_col:
        traffic_light.tlColor="Green"
    else:
        traffic_light.tlColor="Orange"

    sig = tl_position / 5.5

    # print(sig)

    case1Distance = fuzz.gaussmf(tl_position - car_position, 0, sig)
    case1Light = trimf(tl_state, 0, traffic_light.red_col, traffic_light.red_col)

    if case1Distance > case1Light:
        case1 = case1Distance
    else:
        case1 = case1Light

    case2Distance = fuzz.gaussmf(tl_position - car_position, tl_position / 2, sig)
    case2Light = trimf(tl_state, traffic_light.red_col, traffic_light.red_col + traffic_light.orange_col,
                       traffic_light.red_col + traffic_light.orange_col + traffic_light.green_col)

    if case2Distance > case2Light:
        case2 = case2Distance
    else:
        case2 = case2Light

    case3Distance = fuzz.gaussmf(tl_position - car_position, tl_position, sig)
    case3Light = trimf(tl_state, traffic_light.red_col + traffic_light.orange_col, traffic_light.red_col +
                       traffic_light.green_col, traffic_light.red_col + traffic_light.orange_col +
                       traffic_light.green_col)

    if case3Distance > case3Light:
        case3 = case3Distance
    else:
        case3 = case3Light

    carSpeedChoice = case1*0 + case2*1/2 + case3

    textsurface = myfont.render('Slow Down: '+str('%.3f' % case1), False, (0, 0, 0))
    DISPLAY.blit(textsurface, (WIDTH-185, HEIGHT/2-80))

    textsurface = myfont.render('Maintain Speed: '+str('%.3f' % case2), False, (0, 0, 0))
    DISPLAY.blit(textsurface, (WIDTH-185, HEIGHT/2-60))

    textsurface = myfont.render('Speed Up: '+str('%.3f' % case3), False, (0, 0, 0))
    DISPLAY.blit(textsurface, (WIDTH-185, HEIGHT/2-40))

    textsurface = myfont.render('Car Position: ' + str('%.3f' % car_position), False, (0, 0, 0))
    DISPLAY.blit(textsurface, (WIDTH-185, HEIGHT/2-20))

    result_of_aggression = carSpeedChoice/3
    return result_of_aggression


WIDTH = 1080
HEIGHT = 400

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Times New Roman', 14)

DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))

carSpeed = 1
car = Car(0, HEIGHT/2+20 - HEIGHT/4, carSpeed, DISPLAY)
moving = False

tlPlacement = WIDTH*85/100
tlColor = "Green"
traffic_light = TrafficLight(tlPlacement, HEIGHT*0.1, DISPLAY)

percentageOfSpeed = 0
road = Road(0, HEIGHT/2 - HEIGHT/4, WIDTH, HEIGHT, DISPLAY)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    DISPLAY.fill((200, 200, 200))
    road.draw()
    car.move(fuzzy_logic(traffic_light.state, tlPlacement - tlPlacement * 0.03, car.x))
    car.draw()
    traffic_light.update()
    traffic_light.draw()
    pygame.display.update()


