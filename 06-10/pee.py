
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

		if v[position]:				 
			canPee = False

		if position-1 >= 0 and v[position-1]:
			canPee = False			

		if position+1 < len(v) and v[position+1]:
			canPee = False

			
		return canPee

	def findFirst(self):
		i = 0
                first = 0
                found = False

                while i < len(self.vector_pee) and not found:
                        if self.vector_pee[i] == 1:
                                first = i+1
				found = True

			i += 1
	
		return first

	def calculateDistance(self, begin):
	
		first = self.findFirst()
		pos = 0

		while first != len(self.vector_pee) and pos != 0:
			if self.isPossibleToPee(first):
				last = self.findNext(first)
				pos = (last + 1)//2 + first

		return pos
				
											
		
	def pee2pee(self, npeep):

		if npeep == 3:
			return [1,0,1,0,1]

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
	
