from  User import  User
from  AI import  AI



class Game:
    def __init__(self):
        self.user = User()
        self.board_user = self.user.board_player
        self.ai = AI()
        self.board_ai = self.ai.board_player

    def random_board(self): #метод генерирует случайную доску.

    def greet(self): #метод, который в консоли приветствует пользователя

    def loop(self): #  метод с самим игровым циклом

    def start(self): #запуск игры