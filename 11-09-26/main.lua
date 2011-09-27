require 'read_tiles'

function love.load()

    Tileset = love.graphics.newImage('countryside.png')

    local TileW, TileH = 32, 32
    local TilesetW, TilesetH = Tileset:getWidth(), Tileset:getHeight()

    Grass = love.graphics.newQuad(0, 0, TileW, TileH, TilesetW, TilesetH)
    Box = love.graphics.newQuad(32, 0, TileW, TileH, TilesetW, TilesetH)
    Flower = love.graphics.newQuad(0, 32, TileW, TileH, TilesetW, TilesetH)

    File = io.open("tileset.txt", "r")
    TileString = File:read("*all")
    TileArray = read_tiles(TileString)

end

function love.draw()

    local tile_table = { G = Grass, B = Box, F = Flower }

    for i,elem in ipairs(TileArray) do
        for j, elemin in ipairs(elem) do
            local tile_type = tile_table[elemin]

            love.graphics.drawq(Tileset, tile_type, 0 + (j-1)*32, 200 + (i-1)*32)
        end
    end

end
