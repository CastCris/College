#include<stdio.h>
#include<stdlib.h>
#include<string.h>
//
int main(){
	printf("\n");
	int ponte;
	char*inp=(char*)malloc(200*sizeof(*inp)),*split;
	printf("Insira valores inteiros(uma linha): ");
	fgets(inp,100,stdin);
	printf("Os seus modulos sao, respectivamente: ");
	for(int i=0;split=strtok_r(inp," ",&inp);++i){
		ponte=atoi(split);
		ponte<0?ponte*=-1:ponte;
		printf("%i ",ponte);
	}
	printf("\n\n");
	free(inp);
	return 0;
}
