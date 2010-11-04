import unittest

from pee import Mictorium

class testPee(unittest.TestCase):
	
	def setUp(self):
		self.mict1 = Mictorium([0])
		self.mict2 = Mictorium([0,0])
		self.mict3 = Mictorium([0,0,0])
		self.mict4 = Mictorium([1,0])


	def testOnePersonOneMictorium(self):
		self.assertEqual( self.mict1.pee2pee(1), [12] )
	
	def testOnePersonTwoMictoriums(self):
		self.assertEqual( self.mict2.pee2pee(1), [1,0] )

	def testZeroPersonTwoMictoriums(self):
		self.assertEqual( self.mict2.pee2pee(0), [0,0] )

	def testTwoPersonTwoMictoriums(self):
		self.assertEqual( self.mict2.pee2pee(2), [1,0] )
	
	def testTwoPersonThreeMictoriums(self):
		self.assertEqual( self.mict3.pee2pee(2), [1,0,1])

	def testCanIPee(self):
		self.assertEqual( self.mict3.isPossibleToPee(2), True)
		self.assertEqual( self.mict4.isPossibleToPee(1), False )
		self.assertEqual( self.mict4.isPossibleToPee(0), False )


unittest.main()
