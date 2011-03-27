    
class PokerHand

    # str => int
    def value(a_card)
        dict = { 'T'[0] => 10, 'J'[0] => 11,'Q'[0] => 12,'K'[0] => 13} 
        return dict[ a_card[0] ] || (a_card[0]-48)
    end
    
    def suit(a_card)
        return a_card[1]
    end
    
    def initialize(cards)
        @cards = cards
    end
    
    def status      
        if has_equals?(3)
            return 'Three Of A Kind'
        end
        if has_equals?(2)
           return 'One Pair' 
        end
        if is_straight?
            return 'Straight'
        end
    
        return 'No Hand'
    end
    
    #protected
    
    def has_equals?(n)
        @cards.each do |card|
            cont = 0
            @cards.each do |card2|
                cont += 1 if card[0] == card2[0]
            end
            return true if cont == n
        end 
        return false
    end
    
    def is_straight?
        seq = (@cards.map do |c|
            value(c)
        end).sort
        4.times do |n|
            if not seq[n] == seq[n+1]-1
                return false
            end
        end
        return true
    end
    
end
