class Game:
    def __init__(self,size):
        self.size = size
        self.board = [['.' for _ in range(size+1)] for _ in range(size+1)]
        self.dx    = [ 1,-1, 0, 0]
        self.dy    = [ 0, 0, 1,-1]
        self.turn  = True
        self.board[0][0]='0'
        for i in range(0,size):
            self.board[0][i+1]=str(i+1)
            self.board[i+1][0]=str(i+1)
        self.lastPass=False

    def __repr__(self):
        s=[]
        for row in self.board:
            s.append(' '.join(row))
        return '\n'.join(s)
    def valid(self,row,col):
        ''' Check if given cell lies inside the board '''
        return row > 0 and col > 0 and row<=self.size and col <=self.size

    def whoseTurn(self):
        if self.turn:
            return 'x'
        return 'y'
    def toogleTurn(self):
        self.turn = not self.turn

    def adjecentOf(self,row,col):
        adj = [(row+x,col+y) for x,y in zip(self.dx,self.dy) if self.valid(row+x,col+y) ]
        return adj

    def freeCell(self,row,col):
        adj = self.adjecentOf(row,col)
        cell = self.board[row][col]
        for i,j in adj:
            trycell = self.board[i][j]
            if  trycell =='.':
                # print(i,j)
                return True
        return False


    def freeString(self,row,col):
        '''return True if the given cell belong to a string with no liberties'''
        vis ={}
        def dfs(row,col):
            # print(row,col,self.board[row][col])
            vis[(row,col)]=1
            if  (self.freeCell(row,col)):
                return True
            adj = self.adjecentOf(row,col)
            for tryrow,trycol in adj:
                if  (tryrow , trycol) in vis or self.board[tryrow][trycol]!=self.board[row][col]:
                    continue
                if  dfs(tryrow,trycol):
                    return True
            return False
        return dfs(row,col)


    def removeString(self,row,col):
        vis = {}
        def dfs(row,col,char):
            vis[(row,col)]=1
            self.board[row][col]='.'
            for tryrow,trycol in self.adjecentOf(row,col):
                if ((tryrow,trycol) in vis or self.board[tryrow][trycol]!=char):
                    continue
                dfs(tryrow,trycol,char)
        dfs(row,col,self.board[row][col])

    def selfCapture(self,row,col):
        self.board[row][col] = self.whoseTurn()
        ret = self.freeString(row,col)
        self.board[row][col] = '.'
        return not ret

    def capture(self,row,col):
        ret = False
        self.board[row][col]=self.whoseTurn()
        for tryrow,trycol in self.adjecentOf(row,col):
            if self.board[row][col]!= self.board[tryrow][trycol]:
                if not self.freeString(tryrow,trycol):
                    self.removeString(tryrow,trycol)
                    ret = True
        self.board[row][col]='.'
        return ret

    def checkPlay(self,row,col):

        if not self.valid(row,col):
            return False
        if self.board[row][col]!= '.':
            return False
        print(self.selfCapture(row,col) ,  self.capture(row,col))
        if  self.selfCapture(row,col):
            if  self.capture(row,col):
                return True
            else:
                return False
        return True




    def play(self,row,col):
        if not self.checkPlay(row,col):
            return False
        else:
            self.board[row][col] = self.whoseTurn()
            # self.capture(row,col)
            self.toogleTurn()
            self.lastPass = False
            return True
    def Pass(self):
        if self.lastPass:
            return True
        self.lastPass = True
        self.toogleTurn()
        return False

    def countPoints(self):
        x,y=0,0
        for row in self.board:
            for col in row:
                if col.lower() =='x':
                    x+=1
                elif col.lower() =='y':
                    y+=1
        return x,y
    def endGame(self):
        # vis =set()
        def fill(row,col,inv,me):
            # print(row,col)
            # vis.add((row,col))
            if self.board[row][col]==inv:
                self.board[row][col]='D'
            elif self.board[row][col] =='.':
                self.board[row][col]=me

            for trow,tcol in self.adjecentOf(row,col):
                if self.board[trow][tcol] =='.' or self.board[trow][tcol]==inv:
                    fill(trow,tcol,inv,me)
        # def filly(row,col):

        for row in range(1,1+self.size):
            for col in range(1,1+self.size):
                cell = self.board[row][col]
                if  cell =='x':
                    fill(row,col,'Y','X')
                elif cell =='y':
                    fill(row,col,'X','Y')
        return self.countPoints()


# x=Board(9)

# x.board[7][9]='x'
# x.board[8][9]='y'
# x.board[6][9]='y'
# x.play(1,9)
# x.play(7,8)
# x.play(7,9)
# x.play(1,9)
# x.play(9,9)
# x.removeString(9,9)
# print(x.capturedString(9,9))
# print(x.libertiesOf(9,9))
# print(x.libertiesOf(8,9))
# print(x.libertiesOf(3,4))
