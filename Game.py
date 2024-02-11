from random import randint

from User import User
from AI import AI
from Board import Board
from Ship import Ship
from Dot import Dot


class Game:
    # def __init__(self):
    #     u = self.random_board()
    #     ai = self.random_board()
    #     self.user = User(u, ai)
    #
    #     self.ai = AI(ai, u)

    def nev_board(self):
        lens = [3, 2, 2, 1, 1, 1]
        n = ["x+", "y+", "x-", "y-"]
        board = Board()
        count = 0
        for l in lens:
            while True:
                print(l)
                count += 1
                if count > 1000:
                    print(count)
                    return None
                ship = Ship(l, [randint(0, 5), randint(0, 5)], n[randint(0, 3)], l)
                print("ship ", l, ship)
                a = board.add_ship(ship)
                print("yes", a)
                print(board)
                if a!= False:
                    break
                if not a:
                    pass


        return board

    def random_board(self):  # метод генерирует случайную доску.
        board = None
        while board is None:
            board = self.nev_board()
            print("board")
        return board

    def greet(self):  # метод, который в консоли приветствует пользователя
        print("   Игра морскои бой ")
        print("                   ")
        print("   формат ввода: x y ")
        print("   x - номер строки  ")
        print("   y - номер столбца ")

    def loop(self):  # метод с самим игровым циклом
        print(self.user.board_player)

    # print(self.user.board_opponent)

    def start(self):
        # запуск игры
        self.greet()
        self.loop()


a = Game()
print(a.random_board())

# a.user.board_player.next_map()
