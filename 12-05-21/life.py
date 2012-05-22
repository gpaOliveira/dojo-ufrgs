class GameOfLife():
	
	def __init__(self,w,h):
		self.board = []
		self.w = w
		self.h = h
		for i in range(w):
			self.board.append([])
			for j in range(h):
				self.board[i].append(' ')

	def setPos(self,x,y,val):
		self.board[x][y] = val

	def getPos(self, x,y):
		if x >= self.w or x < 0:
			return ' '
		if y >= self.h or y < 0:
			return ' '
		return self.board[x][y]

	def print_me(self):
		print self.board

	def countSurround(self, x, y):
		cont=0
		pointMatrix = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
		for point in pointMatrix:
			if(self.getPos(x+point[0], y+point[1]) == 'x'):
				cont += 1

		return cont

	def nextGer(self):
		extraBoard = []
		for i in range(self.w):
			extraBoard.append([])
			for j in range(self.h):
				extraBoard[i].append(' ')

		for i in range(self.w):
			for j in range(self.h):
				if self.board[i][j] == 'x':
					if (self.countSurround(i,j) < 2 or self.countSurround(i,j) > 3):
						extraBoard[i][j] = ' '
					else:
						extraBoard[i][j] = 'x'
				else:
					if (self.countSurround(i, j) == 3):
						extraBoard[i][j] = 'x'
					else:
						extraBoard[i][j] = ' '

		self.board = extraBoard
