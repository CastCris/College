const find_element=(item,item_index,element,element_positions)=>{
	if(item==element)
		element_positions.push(item_index);
}

const readline=require('readline');
const rl=readline.createInterface({
    input:process.stdin,
    output:process.stdout
});

rl.question('Inset the list for do the search ',(inp_list)=>{
    rl.question('Insert the wish number',(inp_number)=>{

        let tst=inp_list.split(' ').map((x)=>Number(x));
        let number=Number(inp_number);
        //
        let positions=[];
        tst.forEach((item,item_index)=>{
            find_element(item,item_index,10,positions);
            }
        );
        positions.forEach((item,item_index)=>{
            console.log(item,tst[item]);
            }
        );
    });
});
