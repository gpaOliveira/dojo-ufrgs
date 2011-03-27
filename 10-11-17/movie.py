"""General admission 			$11.00 X
Students 						$8.00
Senior Citizens (65 & older) 	$6.00 X
Children (under 13) 			$5.50 
Group (20 people or more) 		$6.00 each

Exceptions
3D movie 							+$3.00 X
Over-length (more than 120 min.) 	+$1.50 X
Movie Day (Thurdsday, except for groups!) 	-$2.00
Weekends 							+$1.50
Loge 								+$2.00"""

class Movie:
	def __init__(self, runtime, day, isParquet, is3D):
		self.runtime = runtime
		self.day = day
		self.isParquet = isParquet
		self.is3D = is3D
		self.tickets = []

	def addTicket(self, age, isStudent):
		price = 11.0

		if age>65:
			price = 6.0

		if isStudent:
			price = min(price,8.0)

		if age < 13:
			price = min(price,5.5)

		price =	self.applyException(price)

		price = self.applyDay(price)

		self.tickets.append(price)

	def applyDay(self, price):
		if self.day == "Thursday":
			price -= 2
		return price

	def applyException(self, price):

		if self.is3D:
			price += 3.0

		if self.runtime>120:
			price += 1.5		

		if self.day in ('Saturday','Sunday'):
			price += 1.5

		return price
		
	def finishPurchase(self):
		
		lenTicket = len(self.tickets)

		if lenTicket < 20: 
			return sum(self.tickets)
		else:
			price = self.applyException(6.0)

			return price * lenTicket
			
