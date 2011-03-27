def fizzBuzz(x):

	saida = ''	
	
	if x % 3 == 0:
		saida += "Fizz"
	if x % 5 == 0:
		saida += "Buzz"
	if x % 11 == 0:
		saida += "Batata"

	if saida == '':
		saida = str(x)

	return saida

if __file__ == 'fizzBuzz.py':
	for i in range(1,166):
		print(fizzBuzz(i))
