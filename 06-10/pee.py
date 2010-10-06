
class Mictorium:
	
	def __init__(self, mict):
		self.mictories_total = len(mict)
		self.vector_pee = mict

	def countEmpty(self):
		empty = 0
		for i in self.vector_pee:
			if i == 0:
				empty += 1

		return empty

	def isEmpty(self):
		
		if self.countEmpty() >= self.mictories_total:
			return True;	 
		
		return False;

	def isPossibleToPee(self, position):
		v = self.vector_pee

		canPee = True

		try:		
			if v[position]:				 
				canPee = False

			if position-1 >= 0 and v[position-1]:
				canPee = False			

			if position+1 <= len(v) and v[position+1]:
				canPee = False

		except:
			return canPee
		
		return canPee
	
	def calculateDistance(self, begin):
		vectorDistances = map(self.vector_pee, 
								lambda i: 0 )

		""" calcula a distance de cada index ate ...."""
		#for mic in self.vectorDistances:
						

	def pee2pee(self, npeep):

		if self.isEmpty() and npeep > 0:
			self.vector_pee[0] = 1;	

		if len(self.vector_pee) < 3:
			return self.vector_pee 

		if not self.isEmpty() and npeep > 1:
			self.vector_pee[2] = 1;
		
		return self.vector_pee

#		if npeep == 0:
#			return [0,0]
#		if self.mictories_total > 1:
#			return [1,0]
#		if npeep == 1:
#			return [1]
	
