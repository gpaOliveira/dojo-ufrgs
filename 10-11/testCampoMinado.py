import unittest

from campoMinado import *

class testCampoMinado(unittest.TestCase):
	def testZeroBombs(self):
		board = ["....", 
				 "....", 
				 "....", 
				 "...."]
		modBoard = campoMinado(board)
		auxFunc = returnNumberMatrix(board)

		self.assertEquals(modBoard,["0000","0000","0000","0000"])

	def testOneBombCorner(self):
		board = ["*...",
				 "....",
				 "....",
				 "...."]
		modBoard = campoMinado(board) 

		self.assertEquals(modBoard,["*100","1100","0000","0000"])

	def testOneBombAuxFunc(self):
		board = ["*...",
				 "....",
				 "....",
				 "...."]

		modBoard = returnNumberMatrix(board)
		
		self.assertEquals(modBoard,[['*',0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])

	def testStringToNumber(self):
		board = [['*',0,0,0],
			[0,0,0,0],
			[0,0,0,0],
			[0,0,0,0]]

		modBoard = returnStringMatrix(board)
		self.assertEquals(modBoard,["*000",
				 "0000",
				 "0000",
				 "0000"] )



	def testOneBombAnotherPlaceAuxFunc(self):
		board = ["....",
				 "....",
				 "....",
				 "...*"]		

		modBoard = returnNumberMatrix(board)

		self.assertEquals(modBoard, [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,'*']])

	def testOneBombOther(self):
		board = ["....",
				 "..*.",
				 "....",
				 "...."]
		modBoard = campoMinado(board) 

		self.assertEquals(modBoard,["0111","01*1","0111","0000"])

	def testReturnAdjacentPoints(self):
		self.assertEquals(listAdjacentPos(0,0), [[1,0],[0,1],[1,1]])

unittest.main()



