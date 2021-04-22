import pygame as pg
from pygame import color
from pygame.locals import *
from threading import Thread, Lock, Event
from renderer import draw_cylinder
from random import randint

pg.init()

window = pg.display.set_mode((800, 450))
pg.display.set_caption('Dale')

h, r = 50, 50
color = (randint(0, 255), randint(0, 255), randint(0, 255))
while True:
    pg.display.update()
    x, y = pg.mouse.get_pos()

    window.fill((0, 0, 0))
    draw_cylinder(window, (x, y), h, r, color)

    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        h -= 0.1
    if keys[pg.K_DOWN]:
        h += 0.1
    if keys[pg.K_LEFT]:
        r -= 0.1
    if keys[pg.K_RIGHT]:
        r += 0.1

    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
        elif event.type == MOUSEBUTTONDOWN:
            color = (randint(0, 255), randint(0, 255), randint(0, 255))
