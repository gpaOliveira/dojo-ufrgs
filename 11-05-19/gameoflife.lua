
function create_matrix(sizex,sizey)
	local matrix = {}
	for i=1,sizex,1 do
		matrix[i] = {}
		for j=1,sizey,1 do 
            matrix[i][j] = false
        end
	end	

	return matrix
end

function copy_matrix(matrix,sizex,sizey)
    local new_matrix = {}

	for i=1,sizex do
		new_matrix[i] = {} 
		for j=1,sizey do
			new_matrix[i][j] = matrix[i][j]
		end
	end

    return new_matrix

end
function is_alive(matrix, x,y)
	return matrix[x][y]
end

function get_vizinhos(matrix, sizex, sizey, x, y)

	local c = 0
	local desloc = { {-1,-1}, {0,-1} , {1,-1},
					 {-1, 0}, 		  {1 , 0},
					 {-1, 1}, {0, 1} , {1, 1}
				}
 
	for j=1,8,1 do 
		if  desloc[j][1]+x <= sizex and
			desloc[j][2]+y <= sizey and
			desloc[j][1]+x > 0 and
			desloc[j][2]+y > 0 then
			if is_alive(matrix,desloc[j][1]+x, 					desloc[j][2]+y) then
						c = c+1
			end		
		end
	end

	return c
end

function next_generation(matrix,sizex,sizey)
	local new_matrix = copy_matrix(matrix,sizex,sizey)

	for i=1,sizex do
		for j=1,sizey do
			local nv = get_vizinhos(new_matrix,sizex,sizey,i,j)
			
			if nv < 2 then
				new_matrix[i][j] = false
			end

			if is_alive(new_matrix, i, j) and (nv == 2) then
				new_matrix[i][j] = true
			end

			if nv > 3 then
				new_matrix[i][j] = false
			end

			if nv == 3 then
				new_matrix[i][j] = true
			end
		end
	end


	return new_matrix
end

function print_matrix(matrix, sizex, sizey)
	local new_matrix = {}
	for i=1,sizex do
		new_matrix[i] = {}
		for j=1,sizey do
			if matrix[i][j] == true then
				new_matrix[i][j] = 1
			else
				new_matrix[i][j] = 0
			end
		end
	end

	for i=1,sizex do
		for j=1,sizey do
			io.write(new_matrix[j][i] .. " ")
		end
		print("")
	end
end

