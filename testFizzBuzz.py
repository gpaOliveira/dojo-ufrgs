import unittest
from fizzBuzz import *

class FizzBuzzTest(unittest.TestCase):

	def testTresRetornaFizz(self):
		self.assertEquals("Fizz",fizzBuzz(3))

	def testCincoRetornaBuzz(self):
		self.assertEquals("Buzz",fizzBuzz(5))

	def testUmRetornaUm(self):
		self.assertEquals("1",fizzBuzz(1))

	def testOnzeRetornaBatata(self):
		self.assertEquals("Batata",fizzBuzz(11))		

	def testQuinzeRetornaFizzBuzz(self):
		self.assertEquals("FizzBuzz",fizzBuzz(15))		

	def testCemRetornaBuzz(self):
		self.assertEquals("Buzz", fizzBuzz(100))

unittest.main()
