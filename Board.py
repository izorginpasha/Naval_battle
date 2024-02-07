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
            for i in ship.dots():

                self.status[int(i[0])][int(i[1])] = u'\u2588'

        except:
            print("Ошибка постановки корабля")

    # def contour(self):# обводит корабль по контуру

    def next_map(self):  # выводит доску в консоль в зависимости от параметра hid
        if self.hid == True:
            for i in range(len(self.status)):
                if i == 0: print("  1 2 3 4 5 6")
                for j in range(len(self.status)):
                    if j == 0: print(i + 1, end=' ')
                    print(self.status[i][j], end=' ')
                print()

        return ""

    # def out(self):# для точки (объекта класса Dot)


#
#
# def shot(self):#выстрел по доске


a = Board()
a.add_ship(2, [2, 1], "x+")
print(a.next_map())
