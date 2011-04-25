import random
from copy import copy

class Santa():

	def __init__(self,nameslist):
		self.people = nameslist.split("\n")

	def getPeople(self):
		return self.people
	
	def sorteio(self):
		sorteado = {}
		pegaveis = copy(self.people)

		for person in self.people:
			if(person in pegaveis):
				pegaveis.remove(person)

			randGuy = random.randint(0,len(pegaveis)-1)
			sorteado[person] = pegaveis[randGuy]

			pegaveis.remove(sorteado[person])
			pegaveis.append(person)

		return sorteado
