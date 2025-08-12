function check_prime_number(x){
	for(var i=2;i<=Math.sqrt(x);++i)
		if(!(x%i))
			return false
	return true
}
//
const readline=require('readline');
const rl=readline.createInterface({
    input:process.stdin,
    output:process.stdout
});

rl.question('Insert the suppose number primes ',(inp)=>{
    var inp_list=inp.split(' ');
    inp_list=inp_list.map((x)=>Number(x));

    var result=inp_list.filter(check_prime_number);
    console.log(result);

    rl.close();
})
