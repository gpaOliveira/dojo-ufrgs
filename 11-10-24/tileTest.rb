require 'tile'

describe TileRoom, "Tile Room" do

	it "should be one Tile" do
	    points = [ [0,0], [1,0], [1,1], [0,1] ]
		room = TileRoom.new(points)
		room.tile([1,1]).should == 1
	end

    it "should be two Tiles" do
        points = [ [0,0], [2,0], [2,1], [0,1] ]
		room = TileRoom.new(points)
		room.tile([1,1]).should == 2
    end

    it "should be one Tiles 2" do
        points = [ [0,0], [2,0], [2,1], [0,1] ]
		room = TileRoom.new(points)
		room.tile([2,1]).should == 1
    end
    
    it "should be one Tiles 3" do
        points = [ [0,0], [2,0], [0,1], [2,1] ]
		room = TileRoom.new(points)
		room.tile([2,1]).should == 1
    end
    
    it "should be one Tiles 3" do
        points = [ [0,0], [4,0], [0,1], [4,1] ]
		room = TileRoom.new(points)
		room.tile([2,1]).should == 2
    end

    it "Should be three Tiles (triangle)" do
        points = [ [0,0], [2,0], [0,2], [1,1] ]
        room = TileRoom.new(points)
        room.tile([1,1]).should == 3
    end

end

describe TileRoom, "Test max points" do
    it "should be area" do
        points = [ [0,0], [2,0], [0,1], [2,1] ]
		room = TileRoom.new(points)
		room.maxX.should == 2
		room.maxY.should == 1		
    end   
end

