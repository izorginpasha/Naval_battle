class Board:
    _status = [[0] * 6 for i in range(6)]
    ship_maps = []
    hid = False
    count_shift = int

    @property
    def status(self):
        return self._status

    # def add_ship(self,list):# ставит корабль на доску
    #     try:
    #         for i in list:
    #             self.status[list[]]
    #
    #
    #     except:
    #     else:
    #     finally:
    # def contour(self):# обводит корабль по контуру

    def next_map(self):  # выводит доску в консоль в зависимости от параметра hid
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
print(a.next_map())
