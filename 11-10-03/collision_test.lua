require 'lunatest'
require 'collision'

function test_simple_collision()

    local point = new_Point(0,0)
    local rect = new_Rect( new_Point(0,0), new_Point(1,1) )

    assert_equal(true, collision(rect, point))
end

function test_new_rect()
    local r1 = new_Rect( new_Point(0,0), new_Point(1,1) )
    local r2 = new_Rect( new_Point(1,1), new_Point(0,0) )
    local r3 = new_Rect( new_Point(0,1), new_Point(1,0) )


    assert_equal(r1.top.x, r2.top.x)
    assert_equal(r1.top.y, r2.top.y)
    assert_equal(r1.bottom.x, r2.bottom.x)
    assert_equal(r1.bottom.y, r2.bottom.y)

    assert_equal(r1.top.x, r3.top.x)
    assert_equal(r1.top.y, r3.top.y)
    assert_equal(r1.bottom.x, r3.bottom.x)
    assert_equal(r1.bottom.y, r3.bottom.y)
end

function test_simple_not_collision()

    local point = new_Point(2,0)
    local rect = new_Rect( new_Point(0,0), new_Point(1,1) )

    assert_equal(false, collision(rect, point))

    point.x = 3

    assert_equal(false, collision(rect, point))

    point.x = 0
    point.y = 5

    assert_equal(false, collision(rect, point))

    point.x = 0.5
    point.y = 1.1
    assert_equal(false, collision(rect, point))

end

function test_very_out()

    local point = new_Point(0,-3)
    local rect = new_Rect( new_Point(0,0), new_Point(1,1) )

    assert_equal(false, collision(rect, point))
end

function test_very_in()

local point = new_Point(2,2)
local rect = new_Rect( new_Point(1,1), new_Point(3,3))

    assert_equal(true, collision(rect, point))

end

lunatest.run()
