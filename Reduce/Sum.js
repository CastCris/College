function sum(total,x){
	return total+x;
}
var tst=[1,2,3,4,5,6,7,8];
var result=tst.reduce(sum,0);
console.log(result);
