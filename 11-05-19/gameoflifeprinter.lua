require "gameoflife"
require "lunatest"

local matrix = create_matrix(20,20)
matrix[5][5] = true
matrix[6][5] = true
matrix[7][5] = true
matrix[7][4] = true
matrix[6][3] = true
print_matrix(matrix, 20, 20)

while true do
	matrix = next_generation(matrix,20,20)
	print_matrix(matrix, 20, 20)
	os.execute("sleep 0.5;clear")
	print("")
end


