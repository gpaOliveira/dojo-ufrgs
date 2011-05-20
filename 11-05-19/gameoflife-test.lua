require "lunatest"
require "gameoflife"

function test_create_matrix()

	local matrix = create_matrix(4,4)
	assert_true( table.getn(matrix) == 4 )
    assert_true( table.getn(matrix[1]) == 4 )

	matrix = create_matrix(10,10)
	assert_true( table.getn(matrix) == 10 )
    assert_true( table.getn(matrix[1]) == 10 )

end

function test_new_simple_generation()
	
	local var = create_matrix(5,5)
	var[3][2] = true
	var = next_generation(var, 5, 5)
	assert_false( var[3][2], "test_new_simple_generation deu errado")

end

function test_is_out()
	local matrix = create_matrix(10,10)
	matrix[1][1] = true
	local var = get_vizinhos(matrix, 10, 10, 1, 1)
	assert_equal(var, 0, "is out");

	matrix[9][10] = true
	local var = get_vizinhos(matrix, 10, 10, 10, 10)
	assert_equal(var, 1, "is out");
end

function test_new_generation()
	local matrix = create_matrix(4,4)
	matrix[2][2] = true
	matrix[2][3] = true
	matrix[3][3] = true
	matrix = next_generation(matrix,4,4)
	assert_true(matrix[2][2])
	assert_true(matrix[3][2])
	matrix[3][2] = true
	matrix[4][1] = true
	matrix = next_generation(matrix,4,4)
	assert_false(matrix[3][2])

	print_matrix(matrix, 4, 4)

end

function test_number_of_neighbors()
	local matrix = create_matrix(3,3)
    matrix[2][2] = true

	assert_equal( 
 		get_vizinhos(matrix,3,3,2,2) , 0 ,
		"O cara tem que ter 0 vizinhos"
	)

end




lunatest.run()
