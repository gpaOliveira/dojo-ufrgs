function new_Point(xp, yp)
    return { x = xp, y = yp}
end

function new_Rect(p1, p2)
    local top, bottom
    if (p1.y > p2.y) then
        top = p1
        bottom = p2
    else
        top = p2
        bottom = p1
    end
    if (top.x < bottom.x) then
        top.x,bottom.x = bottom.x,top.x
    end

    return { top = top, bottom = bottom }
end

function collision(rect, point)

--[[    if (point.x < rect.top.x or point.y > rect.top) then
        return false
    else
        return true
    end]]

    if (point.x <= rect.top.x) and (point.y <= rect.top.y) and
       (point.x >= rect.bottom.x) and (point.y >= rect.bottom.y)then
        return true
    else
        return false
    end

end
