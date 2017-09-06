var x = "12.1";
var y = "12.0";
var z = "0.05";

/*
	Adding
	1. add right side of arrays
	2. account for overflow
	3. add left side of array
*/

const bigNumberOperations = {
	mutliply: function multiply(a,b){
	
	},
	add: function sum(a,b,subtract = false){
		var ret = [];
		var decimal1 = findDecimal(a);
		var decimal2 = findDecimal(b);
		var RightLen = Math.max(a.length - decimal1 - 1, b.length - decimal2 - 1);
		var LeftLen = Math.max(decimal1,decimal2);
		var LeftOverflow = 0;
		console.log(
			"Decimal1:",decimal1,
			"\nDecimal2:",decimal2,
			"\nRightLen:",RightLen,
			"\nLeftLen:",LeftLen
		);
		return ret;
	},
	divide: function divide(a,b){},
};

function multiply(a,b){
	
}

function sum(a,b){

}

function findDecimal(arr){
	var selected = 0;
	arr.forEach(function(elt,i){
		if(typeof elt === "string") selected = i;
	});
	return selected;
}

sum(arr,b);