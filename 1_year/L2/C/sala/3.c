#include<stdio.h>
#include<stdlib.h>
#include<string.h>
//
int main(){
	printf("\n");
	float MAX_VALUE=20000000.0,*v=(float*)calloc(2,sizeof(*v)),*ponte=(float*)calloc(1,sizeof(*ponte));
	v[1]=MAX_VALUE;
	char*inp=(char*)malloc(200*sizeof(*inp)),*split;
	printf("Insira, no maximo, 100 valores, em uma linha: ");
	fgets(inp,200,stdin);
	for(int i=0;split=strtok_r(inp," ",&inp);++i){
		*ponte=atof(split);
		*ponte<v[1]?v[1]=*ponte:v[1];
		*ponte>v[0]?v[0]=*ponte:v[0];
	}
	free(ponte);
	free(inp);
	printf("A diferenca entre o maior numero, %.2f, e o menor numero, %.2f, da lista apresentados, e: %.2f\n\n",v[0],v[1],v[0]-v[1]);
	free(v);
	return 0;
}
