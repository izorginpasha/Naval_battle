from random import randint

from Ship import Ship
from Dot import Dot


class Board:
    _status = [[0] * 6 for i in range(6)]
    ship_maps = []
    hid: bool = True
    count_shift = int

    @property
    def status(self):
        return self._status

    def add_ship(self, ship):  # ставит корабль на доску
        try:  # u'\u2588'
            print(ship.dots())
            if (self.out_ship(ship.dots()) != False):
                for i in ship.dots():
                    self.status[i.x][i.y] = "■"
                self.contour(ship.dots())
            else:
                return False

            # for i in ship.dots():
            #     if (True == self.out(i) or self.status[i.x][i.y] == u'\u2588' or self.status[i.x][i.y] == "*"):
            #         ship = []
            #         print("Ошибка постановки корабля")
            #         return False



        except:
            print("Ошибка постановки корабля")
            return False
            # self.status = [[0] * 6 for i in range(6)]

    def out_ship(self, ship_List):
        for i in ship_List:
            if (True == self.out(i) or self.status[i.x][i.y] == "■" or self.status[i.x][i.y] == "*"):
                ship_List = []
                print("Ошибка постановки корабля")
                return False

    def contour(self, ship_list):  # обводит корабль по контуру
        for i in ship_list:
            for x in range(i.x - 1, i.x + 2):
                for y in range(i.y - 1, i.y + 2):
                    if (self.status[x][y] != "■" and x >= 0 and y >= 0):
                        self.status[x][y] = "*"

    def __str__(self):  # выводит доску в консоль в зависимости от параметра hid
        if True == self.hid:
            for i in range(len(self.status)):
                if i == 0: print("  1 2 3 4 5 6")
                for j in range(len(self.status)):
                    if j == 0: print(i + 1, end=' ')
                    print(self.status[i][j], end=' ')
                print()

        return ""

    def out(self, dot):  # для точки (объекта класса Dot)
        if dot.x >= 0 and dot.y >= 0 and dot.x < 6 and dot.y < 6:
            return False
        else:
            return True

    @status.setter
    def status(self, value):
        self._status = value

    def shot(self, dot):  # выстрел по доске add +1
        x = dot.x - 1
        y = dot.y - 1

        if (self.out(dot) == False):
            print(x, y)
            if self.status[x][y] == "■":
                self.status[x][y] = "X"
                return True
            elif self.status[x][y] == "T":
                return False
            elif self.status[x][y] == 0 or self.status[x][y] == "*":
                self.status[x][y] = "T"
                return False

        else:
            return False


#
#
#

# lens = [3, 2]
# n = ["x+", "y+", "x-", "y-"]
# board = Board()
# count = 0
# for l in lens:
#     x = 1
#     while x == 1:
#         print(l)
#         count += 1
#         if count > 1000:
#             print(count)
#             break
#         try:
#             ship = board.add_ship(Ship(l, [randint(0, 5), randint(0, 5)], n[randint(0, 3)], l))
#             print(ship)
#             print("ship ", l, ship)
#             if ship == None:
#                 break
#         except:
#             break
#
#
#
#
# print(board)
# a = Board()
# a.add_ship(Ship(2, [4, 2], "x+",1))
# a.add_ship(Ship(2, [1, 4], "x+",1))
# a.add_ship(Ship(2, [4, 2], "y+",1))
# a.add_ship(Ship(2, [4, 2], "x+",1))
# a.add_ship(Ship(2, [1, 1], "x-",1))
# a.add_ship(Ship(2, [4, 2], "x+",1))
# print(a)
# a.shot(Dot(1, 1))
# a.next_map()
