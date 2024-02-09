from random import randint
from Dot import Dot

from Player import Player


class AI(Player):

    def ask(self):  # выбор случайной точки
        d = Dot(randint(0, 5), randint(0, 5))
        print("Ход компьютера: {d.x + 1} {d.y + 1}")
        return d
# a = AI()
# a.move()