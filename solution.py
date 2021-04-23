from hanoi import Hanoi
from loop import Scene
from time import sleep


def solve(hanoi, size, origin=1, destiny=3, aux=2, update_period=1):
    if size == 1:
        hanoi.move(origin, destiny)
        sleep(update_period)
        return
    solve(hanoi, size - 1, origin, aux, destiny, update_period)
    hanoi.move(origin, destiny)
    sleep(update_period)
    solve(hanoi, size - 1, aux, destiny, origin, update_period)


if __name__ == '__main__':
    hanoi = Hanoi(3)
    Scene.set_draw_func(hanoi.draw)

    solve(hanoi, len(hanoi), update_period=1)
