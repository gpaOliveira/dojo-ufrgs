from vending import *
import unittest

class TestsVendingMachine(unittest.TestCase):

	def testMachineHasNiquel(self):
		self.assertEquals( vending_machine (['N', 'COIN-RETURN']), ['N'])

	def testMachineHasQuarter(self):
		self.assertEquals( vending_machine (['Q','COIN-RETURN']), ['Q'])

	def testMachineHas2Quarters(self):
		self.assertEquals( vending_machine (['Q','Q','COIN-RETURN']),['Q','Q'] )

	def testMachineHasDime(self):
		self.assertEquals(vending_machine (['D','COIN-RETURN']),['D'])

	def testMachineHasMoneyWhenCoinReturn(self):
		self.assertEquals(vending_machine(['D','N','D','Q','Q','D','O','COIN-RETURN']),['D','N','D','Q','Q','D','O'])

	def testMachineHasNotMoney(self):
		self.assertNotEquals(vending_machine(['D','N','D','Q','Q','D']),['D','N','D','Q','Q','D'])

	def testBuyB(self):
		self.assertEquals(vending_machine(['O','GET-B']),['B'])

	def testBuyA(self):
		self.assertEquals(vending_machine(['D','Q','Q','N','GET-A']),['A'])

	def testBuyAWithDollar(self):
		self.assertEquals(vending_machine(['O','GET-A']), ['A','Q','D'])

	def testBuyAWithCoins(self):
		self.assertEquals(vending_machine(['O', 'D', 'GET-A']), ['A', 'Q', 'D', 'D'])

)

#	def testBuyBReturnCoin(self):
#		self.assertEquals(vending_machine(['O','GET-B','RETURN-COIN']),['B'])

unittest.main()
