## bowling.rb
#class Bowling
#  def hit(pins)
#  end

#  def score
#    1
#  end
#end

class URL

	def initialize(url)
		@url = url
		@protocol, rest = @url.split("://")
		@domain, rest   = rest.split("/")
	end

	attr_reader :protocol

	attr_reader :domain

	def path
		a = @url.split('://')[1].split("/")
		a.shift
		return a.join("/")
	end
end 
