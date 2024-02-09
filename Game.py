from random import randint

from User import User
from AI import AI
from Board import Board
from Ship import Ship
from Dot import Dot


class Game:
    def __init__(self):
        u = self.random_board()
        ai = self.random_board()
        self.user = User(u, ai)

        self.ai = AI(ai, u)

    def nev_board(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        n = ["x+", "y+", "x-", "y-"]
        board = Board()
        count = 0
        for l in lens:
            while True:
                count += 1
                if count > 1000:
                    return None
                print(l, [randint(0, 5), randint(0, 5)], n[randint(0, 3)],l)
                ship = Ship(l, [randint(0, 5), randint(0, 5)], n[randint(0, 3)],l)
                try:
                    board.add_ship(ship)
                    break
                except:
                    pass
        return board

    def random_board(self):  # метод генерирует случайную доску.
        board = None
        while board is None:
            board = self.nev_board()
        return board

    # def greet(self):  # метод, который в консоли приветствует пользователя
    #
    # def loop(self):  # метод с самим игровым циклом
    #
    # def start(self):  # запуск игры


a = Game()
print(a.ai)
