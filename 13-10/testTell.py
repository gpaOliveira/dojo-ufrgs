
import unittest
from tell import findTelephone

class testFindPhone(unittest.TestCase):
	
	def testAreturn2(self):
		self.assertEquals(findTelephone('A'),'2')
	
	def testBReturn2(self):
		self.assertEquals(findTelephone('B'),'2')

	def testCReturn2(self):
		self.assertEquals(findTelephone('C'),'2')

	def testABCReturn222(self):
		self.assertEquals(findTelephone('ABC'),'222')

	def testDEFReturn333(self):
		self.assertEquals(findTelephone('DEF'),'333')

	def testGHIReturn444(self):
		self.assertEquals(findTelephone('GHI'), '444')

	def test1Return1(self):
		self.assertEquals(findTelephone('1'), '1')

	def testUltimate1(self):
		self.assertEquals(findTelephone('1-HOME-SWEET-HOME'), '1-4663-79338-4663')

	def testUltimate2(self):
		self.assertEquals(findTelephone('MY-MISERABLE-JOB'), '69-647372253-562')

	def testUltimateFinal(self):
		self.assertEquals(findTelephone('Z'), '9')
		

unittest.main()
