import pygame as pg
from threading import Thread


class Scene:
    def __draw_func(): pass
    args = None
    kwargs = None
    width = 960
    height = 540

    @classmethod
    def set_draw_func(cls, func, *args, **kwargs):
        cls.__draw_func = func
        cls.args = args
        cls.kwargs = kwargs

    @classmethod
    def draw(cls, surface):
        cls.__draw_func(surface, cls.width, cls.height,
                        *cls.args, **cls.kwargs)


def run():
    pg.init()

    window = pg.display.set_mode((Scene.width, Scene.height))
    pg.display.set_caption('Torre de Hanoi')

    while True:
        window.fill((0, 0, 0))

        Scene.draw(window)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.VIDEORESIZE:
                Scene.width = event.w
                Scene.height = event.h

        pg.display.update()


t = Thread(target=run)
t.start()
