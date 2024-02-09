from Board import Board


class Player:
    def __init__(self):
        self.board_player = Board()
        self.board_opponent = Board()

    def ask(self):  # который «спрашивает» игрока, в какую клетку он делает выстрел
        return

    def move(self):  # метод, который делает ход в игре
        while True:
            self.board_opponent.shot(self.ask())



