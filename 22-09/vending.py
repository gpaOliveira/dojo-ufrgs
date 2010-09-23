def vending_machine(list_stuff):

	count = {'N':0, 'D':0, 'Q':0, 'O':0}
	money = 0

	for i in list_stuff:
		if i != list_stuff[-1]:
			count[i] += 1

	money = count['N']*5 + count['D']*10 + count['Q']*25 + count['O']*100

	if list_stuff[-1] == 'COIN-RETURN':
		return list_stuff[0:-1]

	if list_stuff[-1] == 'GET-A':
		if money == 65:
			return ['A']
		if money >= 65:
			return ['A','Q','D']

	if list_stuff[-1] == 'GET-B':
		if money == 100:
			return ['B']
	


