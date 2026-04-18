#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<stdbool.h>
//
int main(){
	printf("\n");
	int e_1,e_2,e_3,quant,m;
	char u[1];
	bool ctrl;
	for(;;){
		quant=0;
		e_1=0;
		ctrl=true;
		char*inp=(char*)malloc(1000*sizeof(*inp)),**slot;
		printf("Insira: ");
		fgets(inp,1000,stdin);
		for(int i=0;i<1000;++i){
			if((int)inp[i]==32){
				++quant;	
			} else if((int)inp[i]<48||(int)inp[i]>57){
				break;
			}
			++e_1;
			ctrl=false;
		}
		if(ctrl){
			break;
		}
		inp[e_1]=' ';
		++e_1;
		e_2=e_3=0;
		slot=(char**)malloc((quant+1)*sizeof(char));
		char*aux=(char*)malloc(200*sizeof(*aux)),*temp;
		for(int i=0;i<e_1;++i){
			if((int)inp[i]==32){
				if(e_2<4){
					temp=(char*)malloc(e_2*sizeof(*temp));
					m=e_2-1;
				}else{
					temp=(char*)malloc(3*sizeof(*temp));
					m=2;
				}
				--e_2;
				for(int j=0;j<3;++j){
					//printf("%c\n",aux[e_2-j]);
					if((int)aux[e_2-j]<48||(int)aux[e_2-j]>57||e_2-j<0){
						break;
					}
					temp[m-j]=aux[e_2-j];
				}
				//printf("%s\n",temp);
				if(atoi(temp)%4==0||(u[0]-'0')%5==0){
					slot[e_3]=(char*)malloc((e_2+1)*sizeof(char));
					for(int j=0;j<e_2+1;++j){
						if((int)aux[e_2-j]<48||(int)aux[e_2-j]>57){
							break;
						}
						slot[e_3][e_2-j]=aux[e_2-j];
					}
					++e_3;
				}
				for(int j=0;j<200;++j){
					aux[j]='_';
				}
				for(int j=0;j<m;++j){
					temp[j]='_';
				}
				e_2=0;
				free(temp);
			} else{
				aux[e_2]=inp[i];
				u[0]=inp[i];
				++e_2;
			}
		}
		printf("n-> ");
		for(int i=0;i<e_3;++i){
			for(int j=0;j<200;++j){
				if((int)slot[i][j]>57||(int)slot[i][j]<48){
					printf(" ");
					break;
				}
				printf("%c",slot[i][j]);
			}
		}
		printf("\n");
		free(inp);
		free(aux);
	}
	printf("Bye, bye\n\n");
	return 0;
}
