import unittest
from santa import *

class SantaTest(unittest.TestCase):

	santa = Santa("Lucas Zawacki\nCristiano Dalbem\nTomas Mattia")

	def testRecebeEntrada(self):
		people = self.santa.getPeople()
		self.assertEquals( people[0], "Lucas Zawacki" )
		self.assertEquals( people[1], "Cristiano Dalbem" )
		self.assertEquals( len(people), 3)
	
	def testSorteioNaoDeveSerReflexivo(self):
		sorteio = self.santa.sorteio()	
		for person in sorteio:
			self.assertNotEquals(sorteio[person], person)

	def testSorteadoEstaNaLista(self):
		sorteio = self.santa.sorteio()
		people = self.santa.getPeople()
		for sorteado in sorteio:
			self.assertTrue(sorteio[sorteado] in people)

	def testSorteioDeveSerInjetor(self):
		sorteio = self.santa.sorteio()
		apareceram = []
		for person in sorteio:
			self.assertTrue(person not in apareceram)
			apareceram.append(person)
	
	def testSorteioDeveSerSobrejetor(self):
		sorteio = self.santa.sorteio()
		people = self.santa.getPeople()
		for person in people:
			self.assertTrue(person in sorteio.values())

unittest.main()
