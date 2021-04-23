import pygame as pg


def draw_cylinder(surface, pos, height, radius, color=(255, 255, 255)):
    cylinder_body = pg.Rect(pos[0] - radius, pos[1], radius*2, height)
    cylinder_top = pg.Rect(pos[0] - radius, pos[1] -
                           radius*0.25, radius*2, radius*0.5)
    cylinder_bottom = pg.Rect(pos[0] - radius, pos[1] - radius *
                              0.25 + height, radius*2, radius*0.5)

    shadow_color = tuple(x*0.9 for x in color)

    pg.draw.ellipse(surface, shadow_color, cylinder_bottom)
    pg.draw.rect(surface, shadow_color, cylinder_body)
    pg.draw.ellipse(surface, color, cylinder_top)
