from Player import Player
from Dot import Dot


class User(Player):

    def ask(self):  # спрашивать координаты точки из консоли
        c = input("Ваш ход: ").split()
        x, y = c
        x, y = int(x), int(y)
        return Dot(x, y)


# a = User()
# a.move()
