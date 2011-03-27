describe('Testes', {
	'constroi [1,2]': function() {
		var r = range('[1,2]')		
		value_of(r.first()).should_be(1)
		value_of(r.last()).should_be(2)
	},

	'constroi (1,3)': function() {
		var r = range('(1,3)')
		value_of(r.first()).should_be(1)
		value_of(r.last()).should_be(3)
	},

	'1 entre [0,2]': function(){
		value_of(range('[0,2]').has(1)).should_be(true);
	},

	'1 entre (0,2]': function(){
		value_of(range('(0,2]').has(1)).should_be(true);
	},

	'1 entre [0,2)': function(){
		value_of(range('[0,2)').has(1)).should_be(true);
	},

	'1 entre (1,2)': function(){
		value_of(range('(1,2)').has(1)).should_be(false);
	},

	'(1,3) intersection [0,4]': function(){
		var i = range('(1,3)').intersection(range('[0,4]'))
		value_of(i.first()).should_be(1)
		value_of(i.last()).should_be(3)
	},

	'constroi [10,10]': function(){
		value_of(range('[10,10]').first()).should_be(10)
		value_of(range('[10,10]').last()).should_be(10)
	},

	'10.2 vazio (10,11)': function(){
		value_of(range('(10,11)').has(10.2)).should_be(true)
	},

	'(1,2) intersection (2,3)': function(){
		value_of(range('(1,2)').intersection(range('(2,3)')).has(3)).should_be(true)
	}

	//'(1,3) intersection [3,5]' : function() 
})
