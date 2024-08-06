#include<stdio.h>
#include<stdlib.h>
#include<string.h>
//
int main(){
	printf("\n");
	int e=0;
	float*v=(float*)calloc(100,sizeof(*v));
	char*inp=(char*)malloc(200*sizeof(*inp)),*split;
	printf("Insira, no maximo, 100 valores(em uma linha): ");
	fgets(inp,100,stdin);
	for(int i=0;split=strtok_r(inp," ",&inp);++i){
		v[i]=atof(split);
		++e;
	}
	for(int i=0;i<e;++i){
		for(int j=0;j<e;++j){
			if(v[i]<v[j]){
				v[j]+=v[i];
				v[i]=v[j]-v[i];
				v[j]-=v[i];
			}
		}
	}
	for(int i=0;i<e;++i){
		printf("%.2f ",v[i]);
	}
	free(v);
	free(inp);
	printf("\n\n");
	return 0;
}
