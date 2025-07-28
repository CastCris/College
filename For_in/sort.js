function swap(array,idx1,idx2){
	array[idx1]+=array[idx2];
	array[idx2]=array[idx1]-array[idx2];
	array[idx1]-=array[idx2];
}
// Algorithms sort
function selection_sort(array){
	for(i in array){
		for(var j=i;j<array.length;++j){
			if(array[i]>array[j]){
				swap(array,i,j);
			}
		}
	}
}

function insert_sort(array){
	for(i in array){
		if(!i)
			continue
		var key=array[i];
		var curr_index=i-1;
		while(curr_index>-1&&array[curr_index]>key){
			array[curr_index+1]=array[curr_index];
			--curr_index;
		}
		array[curr_index+1]=key
	}
}

function shiftUp(array,index){
	new_index=Math.floor((index-1)/2)
	if(!index|array[new_index]<array[index])
		return;
	swap(array,index,new_index);
	shiftUp(array,new_index);
}
function shiftDown(array,index){
	var temp=index;
	if(index*2+1<array.length&&array[index*2+1]<array[temp])
		temp=index*2+1;
	if(index*2+2<array.length&&array[index*2+2]<array[temp])
		temp=index*2+2;
	//
	if(index!=temp){
		swap(array,index,temp);
		shiftDown(array,temp);
	}
}
function heap_sort(array){
	new_arr=[];
	for(i in array){
		new_arr.push(array[i]);
		shiftUp(new_arr,new_arr.length-1);
	}
	while(array.length){
		array.pop();
	}
	while(new_arr.length){
		array.push(new_arr[0]);
		new_arr[0]=new_arr[new_arr.length-1];
		new_arr.pop();
		shiftDown(new_arr,0);
	}
}

function merge(array,idx1,end_idx1,idx2,end_idx2){
	var curr_idx1=idx1;
	var curr_idx2=idx2;
	new_arr=[];
	while(curr_idx1<=end_idx1&&curr_idx2<=end_idx2){
		if(array[curr_idx1]<=array[curr_idx2]){
			new_arr.push(array[curr_idx1]);
			++curr_idx1;
			continue
		}
		new_arr.push(array[curr_idx2]);
		++curr_idx2;
	}
	while(curr_idx1<=end_idx1){
		new_arr.push(array[curr_idx1]);
		++curr_idx1;
	}
	while(curr_idx2<=end_idx2){
		new_arr.push(array[curr_idx2])
		++curr_idx2;
	}
	//
	for(i in new_arr){
		array[idx1+Number(i)]=new_arr[i];
	}
}
function merge_sort(array,idx1,idx2){
	if(idx1>=idx2)
		return;
	let middle=idx1+parseInt((idx2-idx1)/2);
	//
	merge_sort(array,idx1,middle);
	merge_sort(array,middle+1,idx2);

	merge(array,idx1,middle,middle+1,idx2);
}
//
function start_timer(){
	timer_init=performance.now();
}
function end_timer(){
	timer_now=performance.now();
	console.log("The task take "+((timer_now-timer_init)/1000)+"seconds");
}
//
let readline=require('readline');
let rl=readline.createInterface({
    input:process.stdin,
    output:process.stdout
});

rl.question('Insert a list of intergers for be sort ',(inp_list)=>{
    let timer_init;
    let test=inp_list.split(' ').map((x)=>Number(x));

    console.log("Original array ");
    console.log(test);
    /*
    //
    console.log("Mrge_sort");
    array_merge=test.slice()

    start_timer();
    merge_sort(array_merge,0,array_merge.length-1);
    end_timer();

    console.log(array_merge);
    //
    console.log("Heap_sort")
    array_heap=test.slice();

    start_timer()
    heap_sort(array_heap);
    end_timer()

    console.log(array_heap);
    //
    console.log("Insert_sort");
    array_insert=test.slice();

    start_timer()
    insert_sort(array_insert);
    end_timer()

    console.log(array_insert);
    //
    */
    console.log("Selection_sort");
    array_selection_sort=test.slice();

    start_timer()
    selection_sort(array_selection_sort);
    end_timer()

    console.log(array_selection_sort);
    //
});
