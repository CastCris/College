function sum(total,x){
	return total+x;
}

let readline=require('readline');
let rl=readline.createInterface({
    input:process.stdin,
    output:process.stdout
});

rl.question('Insert an array ',(inp_list)=>{
    var tst=inp_list.split(' ').map((x)=>Number(x));
    var result=tst.reduce(sum,0);
    console.log(result);
});
