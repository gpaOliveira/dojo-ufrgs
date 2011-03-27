SIZE = 4

def campoMinado(boardInicial):
	
	board = returnNumberMatrix(boardInicial)
	
	for i in range(len(board)):
		lin	= board[i]	

		for j in range(len(lin) ):
			if board[i][j] == '*':
				pos = listAdjacentPos(i,j)
				for p in pos:
					if board[i+p[0]][j+p[1]] != '*':
						board[i+p[0]][j+p[1]] += 1;

	return returnStringMatrix(board)

def returnNumberMatrix(board):
	
	array = []

	for i in board:
		line = []
		for j in i:
			if j == '*':
				line.append('*')
			else:
				line.append(0)

		array.append(line)

	return array				

def returnStringMatrix(board):
	array = []
	for i in board:
		line = ''
		for j in i:
			if j == '*':
				line += '*'
			else:
				line += str(j)

		array.append(line)

	return array

def listAdjacentPos(i,j):
	points = []
	positions = [ [1,-1],[0,-1],[1,-1],
				  [-1,0], '*',  [1,0],
				  [-1,1],[0,1], [1,1]]
	
	if i==0:
		positions[0] = positions[1] = positions[2] = '*'
	if i==SIZE:
		positions[6] = positions[7] = positions[8] = '*'

	if j==0:
		positions[0] = positions[3] = positions[6] = '*'
	if j==SIZE:
		positions[2] = positions[5] = positions[8] = '*'

	validPositions = []
	for p in positions:
		if p != '*':
			validPositions.append(p) 

	return validPositions
