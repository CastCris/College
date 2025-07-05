function check_prime_number(x){
	for(var i=2;i<=Math.sqrt(x);++i)
		if(!(x%i))
			return false
	return true
}
//
var tst=[1,2,3,4,5,6,7,8,9,10,11,12,13];
var result=tst.filter(check_prime_number);
console.log(result);
