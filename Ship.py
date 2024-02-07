class Ship:
    def __init__(self, length_, start, direction, life):
        self.length_ = length_
        self.start = start
        self.direction = direction
        self.life = life

    def dots(self): #возвращает список всех точек корабля.
        list = []

        for i in range(self.length_):
            if self.direction == "x+":
               list.append(self.start[0]+i)
            elif self.direction == "x-":
                list.append(self.start[0]-i)
            elif self.direction == "y+":
                list.append(self.start[1] + i)
            elif self.direction == "y-":
                list.append(self.start[1] - i)

        return list
# a = Ship(3,[1.2],"x+",3)
# print(a.dots())