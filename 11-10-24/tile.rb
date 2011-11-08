class TileRoom

    attr_reader :maxX, :maxY

    def initialize(points)
        @points = points
        findMax()
    end

    def tile(square)           
        return (@maxX*@maxY)/(square[0]*square[1])
    end
    
    def findMax()
        @maxX=0
        @maxY=0
        
        @points.each do | p |
            if p[0] > @maxX
                @maxX = p[0]
            end
        end
        
        if @points[2][1] > @points[3][1] then
            @maxY = @points[2][1]
        else
            @maxY = @points[3][1]
        end
                    
    end

end
