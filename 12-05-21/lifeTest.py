import unittest
from life import *

class testLife(unittest.TestCase):

	def testCreateBoard(self):
		board = GameOfLife(2,2)
		board.setPos(0,0, 'x')
		board.setPos(0,1, ' ')
		board.setPos(1,0, 'x')
		board.setPos(1,1, ' ')
		self.assertEquals(board.getPos(0,0), 'x')
		self.assertEquals(board.getPos(0,1), ' ')
		self.assertEquals(board.getPos(1,0), 'x')
		self.assertEquals(board.getPos(1,1), ' ')

	def testMatriz(self):
		board = GameOfLife(4,4)
		matriz = [  [' ', ' ', ' ', ' ' ],
					[' ', 'x', ' ', ' ' ],
					[' ', ' ', ' ', 'x' ],
					[' ', ' ', 'x', ' ' ]]

		for i in range(len(matriz)):
			for j in range(len(matriz[i])):
				board.setPos(i,j, matriz[i][j])
		
		for i in range(len(matriz)):
			for j in range(len(matriz[i])):
				self.assertEquals(board.getPos(i,j), matriz[i][j])

	def testGer(self):
		board  = GameOfLife(4,4)
		matriz = [  ['x', 'x', ' ', ' ' ],
					['x', 'x', ' ', ' ' ],
					[' ', ' ', ' ', ' ' ],
					[' ', ' ', ' ', ' ' ]]

		for i in range(len(matriz)):
			for j in range(len(matriz[i])):
				board.setPos(i,j, matriz[i][j])
				
		board.nextGer()
		matriz2 = [ ['x', 'x', ' ', ' ' ],
					['x', 'x', ' ', ' ' ],
					[' ', ' ', ' ', ' ' ],
					[' ', ' ', ' ', ' ' ]]

		for i in range(len(matriz)):
			for j in range(len(matriz[i])):
				self.assertEquals(board.getPos(i,j), matriz2[i][j])

	def testGer2(self):
		board  = GameOfLife(4,4)
		matriz = [  ['x', 'x', ' ', ' ' ],
					['x', 'x', ' ', ' ' ],
					[' ', ' ', ' ', 'x' ],
					[' ', ' ', 'x', ' ' ]]

		for i in range(len(matriz)):
			for j in range(len(matriz[i])):
				board.setPos(i,j, matriz[i][j])
				
		board.nextGer()
		matriz2 = [ ['x', 'x', ' ', ' ' ],
					['x', 'x', 'x', ' ' ],
					[' ', 'x', 'x', ' ' ],
					[' ', ' ', ' ', ' ' ]]

		for i in range(len(matriz)):
			for j in range(len(matriz[i])):
				self.assertEquals(board.getPos(i,j), matriz2[i][j])


	def testCountSurround(self):
		board  = GameOfLife(4,4)
		matriz = [  ['x', 'x', ' ', ' ' ],
					['x', 'x', ' ', ' ' ],
					[' ', ' ', ' ', 'x' ],
					[' ', ' ', 'x', ' ' ]]

		for i in range(len(matriz)):
			for j in range(len(matriz[i])):
				board.setPos(i,j, matriz[i][j])
		self.assertEquals(board.countSurround(1,1), 3)
		self.assertEquals(board.countSurround(0,0), 3)
		self.assertEquals(board.countSurround(3,3), 2)
				

unittest.main()
