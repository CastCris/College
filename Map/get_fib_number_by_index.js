dp_fib=[1,1]
function add_fib_values(type_fib,amount_numbers){
	if(type_fib>dp_fib.length)
		dp_fib=[];
	while(dp_fib.length<type_fib)
		dp_fib.push(1);
	for(var i=0;i<amount_numbers;++i){
		var sum=0;
		for(var j=0;j<type_fib;++j)
			sum+=dp_fib[dp_fib.length-1-j];
		dp_fib.push(sum);
	}
}
function get_index_fib(type_fib,index){
	if(index>dp_fib.length)
		add_fib_values(type_fib,index);
	return dp_fib[index-1];
}

var tst=[1,2,3,4,5,20,7,8,9,10];
var new_arr=tst.map(index=>get_index_fib(2,index));
console.log(new_arr);
