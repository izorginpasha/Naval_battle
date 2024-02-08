from Ship import Ship


class Board:
    _status = [[0] * 6 for i in range(6)]
    ship_maps = []
    hid = True
    count_shift = int

    @property
    def status(self):
        return self._status

    def add_ship(self, ship_len, ship_start, ship_direction):  # ставит корабль на доску
        try:  # u'\u2588'
            ship = Ship(ship_len, ship_start, ship_direction, ship_len)
            print(ship.dots())
            for i in ship.dots():
                self.status[i.x][i.y] = u'\u2588'
            self.contour(ship.dots())

        except:
            print("Ошибка постановки корабля")
            self.status = [[0] * 6 for i in range(6)]

    def contour(self, ship_list):  # обводит корабль по контуру
        for i in ship_list:
            print(i.x, i.y)
            d = i.x + 2
            c = i.y + 2
            for x in range(i.x-1, i.x+2):
                for y in range(i.y-1, i.y+2):
                    print(x, y)
                    if (self.status[x][y] != u'\u2588'):
                        self.status[x][y] = "*"

    def next_map(self):  # выводит доску в консоль в зависимости от параметра hid
        if self.hid == True:
            print(self.status)
            for i in range(len(self.status)):
                if i == 0: print("  1 2 3 4 5 6")
                for j in range(len(self.status)):
                    if j == 0: print(i + 1, end=' ')
                    print(self.status[i][j], end=' ')
                print()

        return ""

    # def out(self):# для точки (объекта класса Dot)
    @status.setter
    def status(self, value):
        self._status = value


#
#
# def shot(self):#выстрел по доске


a = Board()
a.add_ship(2, [1, 2], "x+")
a.next_map()
