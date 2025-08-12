str="Roma";

for(var i=0;i<str.length;++i){
	var spaces="";
	for(var j=0;j<str.length-i;++j)
		spaces+=' ';

	process.stdout.write(spaces);
	index=0
	for(j of str){
		if(index==i){
			process.stdout.write(' '+j+' ');
			index++
			continue;
		}
		process.stdout.write(j);
		index++
	}
	console.log();
}
