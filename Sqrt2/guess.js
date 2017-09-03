var arr = [1,".",1,2,1];
var arr2 = [1,2,"."];
var arr3 = [0,".",1];

/*
	Adding
	1. add right side of arrays
	2. account for overflow
	3. add left side of array
*/

function multiply(arr1,arr2){
	
}

function sum(arr1,arr2){
	var ret = [];
	var decimal1 = findDecimal(arr1);
	var decimal2 = findDecimal(arr2);
	var RightLen = Math.max(arr1.length - decimal1 - 1, arr2.length - decimal2 - 1);
	var LeftLen = Math.max(decimal1,decimal2);
	var LeftOverflow = 0;
	console.log(
		"Decimal1:",decimal1,
		"\nDecimal2:",decimal2,
		"\nRightLen:",RightLen,
		"\nLeftLen:",LeftLen
	);
	
	
	return ret;
}

function findDecimal(arr){
	var selected = 0;
	arr.forEach(function(elt,i){
		if(typeof elt === "string") selected = i;
	});
	return selected;
}

sum(arr,arr2);