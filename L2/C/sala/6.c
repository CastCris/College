#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<stdbool.h>
//
int main(){
	bool ctrl;
	for(;;){
		ctrl=true;
		printf("\n");
		double*v=(double*)calloc(3,sizeof(*v)),delta;
		char*inp=(char*)malloc(20*sizeof(*inp)),*split,*slot;
		printf("X = ");
		fgets(inp,20,stdin);
		for(int i=0;split=strtok_r(inp," ",&inp);++i){
			v[i]=strtod(split,&slot);
			i==1?ctrl=false:ctrl;
		}
		if(ctrl){
			break;
		}
		delta=pow(v[1],2.0)-4.0*v[0]*v[2];
		free(inp);
		if(delta<0){
			printf("Essa equacao nao possui resolucao!\n");
		} else{
			printf("X' = %.2f\nX'' = %.2f\n",(-v[1]+pow(delta,0.5))/(2.0*v[0]),(-v[1]-pow(delta,0.5))/(2.0*v[0]));
		}
		printf("\n");
		free(v);
	}
	printf("Bye, bye!\n");
	return 0;
}
