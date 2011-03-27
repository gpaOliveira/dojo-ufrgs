
require 'poker'

describe PokerHand, "Poker Hands" do
	
	NO_HAND = [ '6C', 'TE', '2O', '8C', '4P' ]	
	ONE_PAIR = [ 'TC', 'TE', '2O', '8C', '4P' ]
	THREE_OF_A_KIND = [ 'TC', 'TE', 'TO', '2O', '8C' ]	
	STRAIGHT = [ '5C', '8E', '4O', '6O', '7C' ]
	
	it "should be No Hand" do
		hand = PokerHand.new(NO_HAND)
		hand.status.should == 'No Hand'
	end
	
	it "shoulbe be One Pair" do
	    hand = PokerHand.new(ONE_PAIR)
	    hand.status.should == 'One Pair'
	end
	
	it "should be Three of a kind" do
	    hand = PokerHand.new(THREE_OF_A_KIND)
	    hand.status.should == 'Three Of A Kind'	
	end
	
	it "should be Straight" do
	    hand = PokerHand.new(STRAIGHT)	    
	    hand.status.should == 'Straight'	
	end
	it " should be Flush" do
	    hand = PokerHand.new(FLUSH)
	    hand.status.should 
	
end

describe PokerHand, "Suit and Values" do

    it "should return the value" do
        hand = PokerHand.new([])
        hand.value('TC').should == 10
        hand.value('6C').should == 6
    end

end
