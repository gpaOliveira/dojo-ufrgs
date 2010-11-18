from movie import Movie

import unittest

class testMovie(unittest.TestCase):
	def setUp(self):
		self.m = Movie(160,"Monday", True, True)

	def testMovieBasic(self):
		# addTicket (age, isStudent)
		self.m.addTicket(30,False)
		price = self.m.finishPurchase()
		self.assertEquals(price,15.50)

	def testMovieEldery(self):
		self.m.addTicket(66, False)
		price = self.m.finishPurchase()
		self.assertEquals(price, 10.50)
		
	def testMovieStudent(self):
		self.m.addTicket(10, True)
		price = self.m.finishPurchase()
		self.assertEquals(price, 10.0)

	def testMovieManyPeople(self):
		for i in range(10):
			self.m.addTicket(22, True)
		price = self.m.finishPurchase()
		self.assertEquals(price, 125.0)
		
	def testMovieManyManyManyPeople(self):
		for i in range(20):
			self.m.addTicket(22, True)
		price = self.m.finishPurchase()
		self.assertEquals(price, 20*10.5 )

	def testMovieThursday(self):
		m = Movie(110, "Thursday", True, True)
		m.addTicket(10,True)
		price = m.finishPurchase()

		self.assertEquals(price,6.5)

	def testGoingWithLotsOfPeopleOnThursday(self):
		m = Movie(110, "Thursday", True, True)
		
		for i in range(30):
			m.addTicket(20+i,True)
		
		price = m.finishPurchase()
		self.assertEquals(price,30 * 9)

	def testMovieWeekend(self):
		m = Movie(121, "Saturday", True, True)

		m.addTicket(20,False)
		price = m.finishPurchase()

		self.assertEquals(price, 17.0)

unittest.main()
