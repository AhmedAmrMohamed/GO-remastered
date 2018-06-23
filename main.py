import tkinter as tk
from Board import *
size = 9
class Game:
    def play(self,row,col):
        turn = self.board.play(row,col)
        if turn:
            self.buttons[row][col].config(bg='grey')
        else:
            self.buttons[row][col].config(bg = 'blue')

    def __init__(self):
        self.board = Board(size)
        self.buttons = [['.' for _ in range(size+1)] for _ in range(size+1)]
        self.root = tk.Tk()
        self.root.geometry('344x372')
        self.redpiece  = tk.PhotoImage(file='rook.png')
        self.bluepiece = tk.PhotoImage(file='checkerPiecesBlue.png')
        self.greypiece = tk.PhotoImage(file='checkerPiecesGrey.png')
        for i in range(1,size+1):
            for j in range(1,size+1):
                b = tk.Button(self.root,bg = 'red',width = 4,height =2,
                   command  = lambda i=i,j=j:self.play(i,j))
                b.grid(row = i,column =j)
                self.buttons[i][j]=b
        self.root.mainloop()
x = Game()
