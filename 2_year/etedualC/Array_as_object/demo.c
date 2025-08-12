#include<math.h>
#include<stdio.h>
#include<stdlib.h>
//
void fill_arr_with_power(int*arr,size_t arr_size,int num){
	for(size_t i=0;i<arr_size;++i){
		arr[i]=pow(num,i);
	}
}
void display_array(int*arr,size_t arr_size){
	for(size_t i=0;i<arr_size;++i)
		printf("%i ",arr[i]);
}

int main(){
	size_t array_size=10;
	int*array=calloc(array_size,sizeof(int));
	//
	display_array(array,array_size);
	printf("\n");

	fill_arr_with_power(array,array_size,2);

	display_array(array,array_size);
	printf("\n");

	return 0;
}
