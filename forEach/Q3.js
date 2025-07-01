dp_fib=[1,1]
function add_fib_values(type_fib,amount_numbers){
	if(type_fib>dp_fib.length){
		add_fib_values(2,type_fib);
	}
	for(var i=0;i<amount_numbers;++i){
		sum=0;
		for(var j=0;j<type_fib;++j)
			sum+=dp_fib[dp_fib.length-1-j];
		dp_fib.push(sum);
	}
}
function get_index_fib(type_fib,index){
	if(index>dp_fib.length)
		add_fib_values(type_fib,index);
	return dp_fib[index];
}

tst=[1,2,3,4,100]
tst.map(num => get_index_fib(2,num))
console.log(tst)
