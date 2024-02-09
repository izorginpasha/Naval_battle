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

    def add_ship(self, ship_len, ship_start, ship_direction):  # ставит корабль на доску
        try:  # u'\u2588'
            ship = Ship(ship_len, ship_start, ship_direction, ship_len)
            for i in ship.dots():
                print(i)
                if (self.out(i) == False):
                    self.status[i.x][i.y] = u'\u2588'
            self.contour(ship.dots())

        except:
            print("Ошибка постановки корабля")
            self.status = [[0] * 6 for i in range(6)]

    def contour(self, ship_list):  # обводит корабль по контуру
        for i in ship_list:
            for x in range(i.x - 1, i.x + 2):
                for y in range(i.y - 1, i.y + 2):
                    if (self.status[x][y] != u'\u2588' and x >= 0 and y >= 0):
                        self.status[x][y] = "*"

    def next_map(self):  # выводит доску в консоль в зависимости от параметра hid
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
            if self.status[x][y] == u'\u2588':
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


# a = Board()
# a.add_ship(2, [2, 2], "x+")
# a.next_map()
# a.shot(Dot(1, 1))
# a.next_map()
