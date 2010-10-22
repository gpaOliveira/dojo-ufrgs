## bowling_spec.rb
#require 'bowling'

#describe Bowling, "#score" do
#  it "returns 0 for all gutter game" do
#    bowling = Bowling.new
#    20.times { bowling.hit(0) }
#    bowling.score.should == 0
#  end
#end

require 'url'

describe URL, "#http" do
	it "returns http for http://www.yeah.com" do
		url = URL.new("http://www.yeah.com")
		url.protocol.should == "http"
	end

	it "should return ftp for ftp://inf.ufrgs.br/~ritt" do
		url = URL.new("ftp://inf.ufrgs.br/~ritt")
		url.protocol.should == "ftp"
	end

	it "should return http for http://inf.ufrgs.br:80/~fernando" do
		url = URL.new("http://inf.ufrgs.br:80/~fernando")
		url.protocol.should == "http"
	end

	it "should return inf.ufrgs.br for http://inf.ufrgs.br/~al" do
		url = URL.new("http://inf.ufrgs.br/~al")
		url.domain.should == "inf.ufrgs.br"
	end

	it "should return www.google.com for ftp://www.google.com" do
		url = URL.new("ftp://www.google.com")	
		url.domain.should == "www.google.com"
	end

	it "should return ~al for http://inf.ufrgs.br/~al" do
		url = URL.new("http://inf.ufrgs.br/~al")
		url.path.should == "~al"
	end

	it "should return ~al/1 for http://inf.ufrgs.br/~al/1" do
		url = URL.new("http://inf.ufrgs.br/~al/1")
		url.path.should == "~al/1"
	end
end
