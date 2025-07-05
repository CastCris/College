const find_element=(item,item_index,element,element_positions)=>{
	if(item==element)
		element_positions.push(item_index);
}
let tst=[1,2,3,10,10,2,3,4,5,10,10];
let positions=[];
tst.forEach((item,item_index)=>{
	find_element(item,item_index,10,positions);
	}
);
positions.forEach((item,item_index)=>{
	console.log(item,tst[item]);
	}
);
