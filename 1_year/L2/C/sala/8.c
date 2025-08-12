#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<stdbool.h>
//
int main(){
	printf("\n");
	int e,e_2,e_3,q_n,quant;
	bool ctrl;
	for(;;){
		char*inp=(char*)malloc(1000*sizeof(*inp)),ult[1];
		printf("Insira: ");
		fgets(inp,1000,stdin);
		ctrl=true;
		e=0;
		for(int i=0;i<1000;++i){
			if((int)inp[i]<48||(int)inp[i]>57){
				if((int)inp[i]!=32){
					break;
				}
			}
			if((int)inp[i]==32){
				++q_n;
			}
			++e;
			ctrl=false;
		}
		if(ctrl){break;}
		e_2=e_3=quant=0;
		inp[e]=' ';
		++e;
		char**ns=(char**)calloc((q_n+1),sizeof(**ns));
		char*temp=(char*)malloc(200*sizeof(*temp));
		for(int i=0;i<e;++i){		
			if((int)inp[i]==32){
				if(quant%3==0&&(ult[0]-'0')%2==0){
					//printf("%c%c\n",temp[0],temp[1]);
					ns[e_3]=(char*)malloc(e_2+1*sizeof(char));
					for(int j=0;j<e_2+1;++j){
						if((int)temp[j]<48||(int)temp[j]>57){
							break;
						}	
						ns[e_3][j]=temp[j];
					}
					++e_3;
				}
				for(int i=0;i<e_2+1;++i){
					temp[i]='_';
				}
				e_2=0;
				quant=0;
			} else{
				quant+=inp[i]-'0';
				ult[0]=inp[i];
				temp[e_2]=inp[i];
				++e_2;
			}

		}
		printf("n-> ");
		for(int i=0;i<e_3;++i){
			for(int j=0;j<strlen(ns[i]);++j){
				if((int)ns[i][j]<48||(int)ns[i][j]>57){
					break;
				}
				printf("%c",ns[i][j]);
			}
			printf(" ");
		}
		printf("\n");
		free(inp);
		free(temp);
		free(ns);
	}
	printf("Bye,bye\n\n");
	return 0;
}
