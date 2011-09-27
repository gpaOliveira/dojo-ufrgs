
function read_tiles(tile_string)

    local linha = 1
    local vetString = {}
    local tamString = #tile_string
    local coluna = 1

    for i=1, tamString do

        if vetString[linha] == nil then
            vetString[linha] = {}
            coluna = 1
        end

        local charizard = string.char(string.byte(tile_string,i))

        if charizard == "\n" then
            linha = linha + 1
        else
            vetString[linha][coluna] = charizard
            coluna = coluna + 1
        end
    end

    return vetString
end

function compare_array(a1, a2)
    for i,j in ipairs(a1) do

        if (type(j) ~= type(a2[i])) then
            return false
        end

        if (type(j) == 'table') then
            if compare_array(j, a2[i]) == false then
                return false
            end
        elseif j ~= a2[i] then
            return false
        end
    end

    return true
end
