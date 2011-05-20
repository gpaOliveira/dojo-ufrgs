require "gameoflife"
require "lunatest"

local matrix = create_matrix(10,10)
matrix[5][5] = true
matrix[6][5] = true
matrix[7][5] = true
matrix[7][4] = true
matrix[6][3] = true
print_matrix(matrix, 10, 10)

while true do
	matrix = next_generation(matrix,10,10)
	print_matrix(matrix, 10, 10)
	os.execute("sleep 1")
	print("")
end


