function range(text_rep){
	values = text_rep.match(/^.([0-9.]+),([0-9.]+).$/);
	var first = parseFloat(values[1])
	var last = parseFloat(values[2])

	var inf = ">" + (text_rep[0]=='(' ? "" : "=")
	var sup = "<" + (text_rep[text_rep.length-1]==')' ? "" : "=")

	return {
		has:function(number){
			return eval(number + inf + first + "&&" + number + sup + last)
		},		

		first: function() {
			return first
		},

		last: function() {
			return last
		},

		intersection: function(a) {
			var f = a.first() < first ? first : a.first()
			var l = a.last() > last ? last : a.last()

			return range("[" + f + "," + l + "]")
		}
	}


}
