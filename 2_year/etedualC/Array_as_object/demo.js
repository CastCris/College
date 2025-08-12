function fill_arr_with_power(object,num){
	for(var i=0;i<object.length;++i)
		object[i]=Math.pow(num,i);
}
var arr=[1,2,3,4,5,6,7,8];
console.log("Original array: "+arr);
fill_arr_with_power(arr,2);
console.log("Final array: "+arr);
