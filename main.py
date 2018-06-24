import tkinter as tk
from tkinter import messagebox
from Game import *
from Inter import *
size = 9
class screen:
    def play(self,row,col):
        self.inter.play(row,col)


        # ms =messagebox.askyesno('sad','dsad')
        # ms.grid(row = 7,column=size+9)
    def __init__(self):
        self.inter = Inter(size,self)
        # self.game = Game(size)
        self.buttons = [['.' for _ in range(size+1)] for _ in range(size+1)]
        self.root = tk.Tk()
        self.root.geometry('600x372')
        self.whoseTurn = tk.StringVar()
        self.whoseTurn.set('Turn to blue')
        for i in range(1,size+1):
            for j in range(1,size+1):
                b = tk.Button(self.root,bg = 'white',width = 4,height =2,
                   command  = lambda i=i,j=j:self.play(i,j))
                b.grid(row = i,column =j)
                self.buttons[i][j]=b
        self.label = tk.Label(self.root,text='Turn To Blue',font ='console 10 bold',padx = 30)
        self.label.grid(row = 3,columnspan = 10,column = size +9)
        self.Pass = tk.Button(self.root,text='Pass',font ='console 10 bold',padx =10,command = self.inter.Pass)
        self.Pass.grid(row = 6,columnspan =10,column = size+9)
        self.root.mainloop()
x = screen()
