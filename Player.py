from Board import Board


class Player:
    def __init__(self, board_player, board_opponent):
        self.board_player = board_player
        self.board_opponent = board_opponent

    def ask(self):  # который «спрашивает» игрока, в какую клетку он делает выстрел
        return

    def move(self):  # метод, который делает ход в игре
        while True:
            self.board_opponent.shot(self.ask())
            print(self.board_player)
