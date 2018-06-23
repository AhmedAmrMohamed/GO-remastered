class Board:
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

    def __repr__(self):
        s=[]
        for row in self.board:
            s.append(' '.join(row))
        return '\n'.join(s)
    def valid(self,row,col):
        ''' Check if given cell lies inside the board '''
        return row >= 0 and col >= 0 and row<=self.size and col <=self.size

    def whoseTrun(self):
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
                print(i,j)
                return True
        return False


    def freeString(self,row,col):
        '''return True if the given cell belong to a string with no liberties'''
        vis ={}
        def dfs(row,col):
            print(row,col,self.board[row][col])
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
        self.board[row][col] = self.whoseTrun()
        ret = self.freeString(row,col)
        self.board[row][col] = '.'
        return not ret

    def checkPlay(self,row,col):
        if not self.valid(row,col):
            raise Exception('invalid input')
            return False
        if  self.selfCapture(row,col):
            raise Exception('selfCapture')
            return False
        return True

    def capture(self,row,col):
        for tryrow,trycol in self.adjecentOf(row,col):
            if self.board[row][col]!= self.board[tryrow][trycol]:
                if not self.freeString(tryrow,trycol):
                    self.removeString(tryrow,trycol)

    def play(self,row,col):
        if not self.checkPlay(row,col):
            return False
        else:
            self.board[row][col] = self.whoseTrun()
            self.capture(row,col)
            self.toogleTurn()
            return True

x = Board(9)
# print(x)
x.board[9][9]='y'
x.board[9][8]='x'
x.board[8][9]='y'
x.board[7][9]='y'
x.board[8][8]='x'
x.board[7][8]='x'
x.board[6][9]='x'
# x.board[7][9]='x'
# x.play(8,9)
# x.play(7,9)
# x.play(1,9)
# x.play(9,9)
# x.removeString(9,9)
# print(x.capturedString(9,9))
# print(x.libertiesOf(9,9))
# print(x.libertiesOf(8,9))
# print(x.libertiesOf(3,4))
