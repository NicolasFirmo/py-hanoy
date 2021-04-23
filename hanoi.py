from renderer import draw_cylinder
from loop import Scene
from time import sleep


class Hanoi:
    PADDING = 150

    def __init__(self, number_of_discs):
        self.__size = number_of_discs
        self.__towers = (list(range(number_of_discs, 0, -1)), [], [])

    def move(self, origin, destiny):
        if not self.__towers[destiny - 1]:
            self.__towers[destiny - 1].append(self.__towers[origin-1].pop())
        elif self.__towers[origin-1][-1] < self.__towers[destiny - 1][-1]:
            self.__towers[destiny - 1].append(self.__towers[origin-1].pop())

    def draw(self, surface, width, height):
        for index, tower in enumerate(self.__towers):
            self.__draw_tower(surface,
                              ((index + 1)*width/4, height - self.PADDING),
                              height/self.__size/3, width/self.__size/15,
                              0.8, tower)

    def __draw_tower(self, surface, pos, disc_height, small_radius,
                     growth_factor, discs):
        y = pos[1]
        for disc in discs:
            draw_cylinder(surface, (pos[0], y), disc_height,
                          small_radius * 2 * disc * growth_factor)
            y -= disc_height

if __name__ == '__main__':
    hanoi = Hanoi(5)
    Scene.set_draw_func(hanoi.draw)  # necessário para renderizar a torre na tela

    sleep(1)
    hanoi.move(1, 3)
    sleep(1)
    hanoi.move(1, 2)
    sleep(1)
