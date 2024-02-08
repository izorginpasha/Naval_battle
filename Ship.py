from Dot import Dot


class Ship:
    def __init__(self, length_, start, direction, life):
        self.length_ = length_
        self.start = start
        self.direction = direction
        self.life = life

    def dots(self):  # возвращает список всех точек корабля.
        list = []
        try:
            for i in range(self.length_):

                if self.direction == "x+":
                    list.append(self.dot(self.start[1] - 1, self.start[0] + (i - 1)))
                elif self.direction == "x-":
                    list.append(self.dot(self.start[1] - 1, self.start[0] - (i + 1)))
                elif self.direction == "y+":
                    list.append(self.dot(self.start[1] + i - 1, self.start[0] - 1))
                elif self.direction == "y-":
                    list.append(self.dot(self.start[1] - i - 1, self.start[0] - 1))


            return list
        except:
            return False
    def dot(self, point_x, point_y):
        try:
            if (point_x >= 0 and point_y >= 0):
                return Dot(point_x, point_y)
            else:
                return exit()
        except:
            print("ошибка точки")

# a = Ship(3, [1, 1], "x+", 3)
# b = a.dots()
# print(b)
