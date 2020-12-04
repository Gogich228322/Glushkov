
let arr = [-2, -1, 0, 1, 2, 3]; 
console.log(arr.filter(elem => elem > 0));



let arr2 = [-2, -1, 0, 1, 2, 3]; 
console.log(arr2.filter(elem => elem < 0));


let arr3 = [-3, -2, -1, 0, 1, 3, 5, 10, 15, 20];
console.log(arr3.filter(elem => elem > 0 && elem < 10));


let arr4 = ['Kek', 'check', 'chebyrek', 'artemiy'];
console.log(arr4.filter(elem => elem.length > 5));


let arr5 = [-3, -1, 0, 1, 3, 6, 15, 20, 50];
let result = arr5.filter(function(elem, index) {
	return elem * index < 30;
});

console.log(result); 


let arr6 = [1, 2, [3, 4], 5, [6, 7]];
let result2 = arr6.filter(function(elem){
	if(Array.isArray(elem)) {
		return false;
	} else {
		return true;
	}
});

console.log(result2);


let arr7 = [-3, -5, -2, 0, 4, 2, 5];
console.log(arr7.filter(elem => elem < 0).length);
