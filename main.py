from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from random import randint
from kivy.config import Config


class Cell(Button):
    def __init__(self, isBomb, **kwargs):
        super(Button, self).__init__(**kwargs)
        self.isBomb = isBomb
        self.isRevealed = False
        self.neighbors = []
        self.num = 0
        self.bind(on_press=self.reveal)

    def countNeighborBomb(self):
        for n in self.neighbors:
            if n.isBomb:
                self.num += 1
        if(not self.num == 0 and not self.isBomb and self.isRevealed):
            self.text = str(self.num)

    def reveal(self, instance):
        self.isRevealed = True

        if(self.isBomb):
            self.background_color = (1, 0, 0, 1)
            App.get_running_app().root.reset()
        else:
            self.background_color = (0.5, 0.5, 0.5, 1.0)
            if(self.num != 0):
                self.text = str(self.num)
            else:
                for n in self.neighbors:
                    if(not n.isRevealed and not n.isBomb):
                        n.reveal(n)

    def setBomb(self):
        self.isBomb = True


class Board(GridLayout):
    def __init__(self, rows, cols, bombs, **kwargs):
        super(Board, self).__init__(**kwargs)
        self.cols = cols
        self.rows = rows
        self.bombs = bombs
        self.buildBoard()

    def validCell(self, i, j):
        return 0 <= i < self.rows and 0 <= j < self.cols

    def reset(self):
        self.clear_widgets()
        self.buildBoard()

    def buildBoard(self):
        self.resetBoard()
        self.setNeighbors()
        self.setBombs()
        self.assignBoard()

    def setNeighbors(self):
        for i in range(self.rows):
            for j in range(self.cols):
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if self.validCell(i + x, j + y):
                            self.board[i][j].neighbors.append(self.board[i + x][j + y])

    def setBombs(self):
        for _ in range(self.bombs):
            c = None
            while(not c or c.isBomb):
                i = randint(0, self.rows - 1)
                j = randint(0, self.cols - 1)
                c = self.board[i][j]
            c.setBomb()

    def resetBoard(self):
        self.board = [[Cell(False) for x in range(self.cols)] for y in range(self.rows)]

    def assignBoard(self):
        for bs in self.board:
            for b in bs:
                b.countNeighborBomb()
                self.add_widget(b)


class Game(App):
    def build(self):
        return Board(20, 10, bombs=25)


if __name__ == "__main__":
    Config.set('graphics', 'width', '500')
    Config.set('graphics', 'height', '1000')
    Game().run()
