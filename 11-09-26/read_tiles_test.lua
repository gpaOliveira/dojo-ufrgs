require "lunatest"
require "read_tiles"

function test_string_simples()

    -- { "B" }
    local tiles = read_tiles("G")

    assert_equal(tiles[1][1], "G")

    tiles = read_tiles("B")
    assert_equal(tiles[1][1], "B")

end

function test_compare_array()

    local a1 = {"G"}
    local a2 = {"B"}
    assert_equal(false, compare_array(a1,a2))

    assert_equal(true, compare_array(a1,a1))
end

function test_string_mais_complicada()

    local other={ {"G","G","G"} }

    local tiles = read_tiles("GGG")
    assert_equal(compare_array(tiles, other),true)

    local other2 = {{"G","G","G"},{"G","G","G"}}

    tiles = read_tiles("GGG\nGGG")
    assert_equal(compare_array(tiles, other2),true)

    local other3 = {{"G","G","G"},{"G","B","G"},{"B","B","G"}}
    tiles = read_tiles("GGG\nGGG")
    assert_equal(compare_array(tiles, other3), false)

end

function test_array_meio_louco()

    local other3 = {{"G"},{"G","B","G"},{"B","B","G"}, {"H","H"}}
    tiles = read_tiles("G\nGBG\nBBG\nHH")
    assert_equal(compare_array(tiles, other3), true)

end

lunatest.run()
