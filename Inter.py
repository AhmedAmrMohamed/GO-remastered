from Game import *
from tkinter import messagebox
class Inter:
    def __init__(self,size,scr):
        self.size = size
        self.game = Game(size)
        self.screen = scr

    def play(self,row,col):
        ret = self.game.play(row,col)
        self.update()

    def update(self):
        board = self.game.board
        self.screen.Pass.config(bg='white')
        for row in range(1,1+self.size):
            for col in range(1,1+self.size):
                if board[row][col] =='x':
                    self.screen.buttons[row][col].config(bg = 'blue')
                elif board[row][col] =='y':
                    self.screen.buttons[row][col].config(bg = 'red')
                else:
                    self.screen.buttons[row][col].config(bg = 'white')

        print(self.game.whoseTurn(),self.screen.whoseTurn.get())
        if self.game.whoseTurn()=='x':
            self.screen.label.config(text = 'Turn To Blue')
        else:
            self.screen.label.config(text = 'Turn To Red ')

    def Pass(self):
        if not self.game.Pass():
            if self.game.whoseTurn() =='x':
                self.screen.Pass.config(bg = 'red')
            else:
                self.screen.Pass.config(bg = 'blue')
            return
        x,y=self.game.endGame()
        # print(self.game)
        title = 'Congratularions '
        msg = 'as'
        if(x>y):
            title += 'BLUE'
        elif x<y:
            title +='RED'
        else:
            title ='TIE'
        msg ='Blue = {} : RED = {}'.format(x,y)
        msg+='\n click OK to exit'
        messagebox.showinfo(title,msg)
        self.screen.root.destroy()
