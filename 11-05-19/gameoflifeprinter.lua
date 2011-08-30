require "gameoflife"
require "lunatest"

local matrix = create_matrix(25,25)

matrix[13][13] = true
matrix[13][14] = true
matrix[13][15] = true
matrix[12][14] = true
matrix[14][13] = true

print_matrix(matrix, 25, 25)

while true do
	matrix = next_generation(matrix,25,25)
	print_matrix(matrix, 25, 25)
	os.execute("sleep 0.25;clear")
	print("")
end

