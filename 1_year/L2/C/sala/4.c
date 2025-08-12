#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<stdbool.h>
//
int main(){
	bool cont;
	printf("\n");
	for(;;){
		cont=true;
		bool para=false,e=true;
		float*v=(float*)calloc(3,sizeof(*v));
		char*inp=(char*)malloc(20*sizeof(*inp)),*split;
		printf("Insira os lados de um triangulo(uma linha): ");
		fgets(inp,20,stdin);
		for(int i=0;split=strtok_r(inp," ",&inp);++i){
			if(i>2){
				printf("Oxente, desde quando isso e um triangulo?\n");
				para=true;
				break;
			}
			i==1?cont=false:cont;
			v[i]=atof(split);
		}
		if(cont){
			break;
		}
		free(inp);
		if(!para){
			float aux=0.0;
			for(int i=0;i<3;++i){
				for(int j=0;j<3;++j){
					j!=i?aux+=v[j]:aux;
				}
				if(v[i]>aux){
					printf("Oxente, desde quando isso e um triangulo?\n");
					e=false;
					break;
				}
				aux=0;
			}
			if(e){
				char*out=(char*)malloc(15*sizeof(*out));
				out="Equilatero";
				v[0]!=v[1]&&v[1]!=v[2]&&v[0]!=v[2]?out="Escaleno":v[0]==v[1]&&v[1]!=v[2]?out="Isoceles":v[1]==v[2]&&v[1]!=v[0]?out="Isoceles":v[0]==v[2]&&v[2]!=v[1]?out="Isoceles":out;
				printf("Ok...\no tipo do triangulo e: %s\n\n",out);
			}
		}
		free(v);
	}
	printf("Bye, bye!\n\n");
	return 0;
}
