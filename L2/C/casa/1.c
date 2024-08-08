#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<stdbool.h>
//
int main(){
    bool ctrl;
    int q,e_1,e_2,e_3;
    char u[1],*inp,**par,*aux;
    for(;;){
   	 q=e_1=e_2=e_3=0;
   	 ctrl=true;
   	 inp=(char*)malloc(1000*sizeof(*inp));
     printf("Insira os valores: ");
   	 fgets(inp,1000,stdin);
   	 for(int i=0;i<1000;++i){
   		 if(inp[i]==32){
   			 ++q;
   		 }else if((int)inp[i]<48||(int)inp[i]>57){
   			 break;
   		 }
   		 ctrl=false;
   		 ++e_1;
   	 }
   	 inp[e_1]=' ';
   	 ++e_1;
   	 if(ctrl)
   		 break;
   	 par=(char**)malloc((q+1)*sizeof(char*));
   	 aux=(char*)malloc((e_1+1)*sizeof(char));
   	 for(int i=0;i<e_1;++i){
   		 if((int)inp[i]==32){
   			 if((u[0]-'0')%2==0){
   				 par[e_3]=(char*)malloc((e_2-1)*sizeof(char));
   				 for(int j=0;j<e_2;++j){
   					 //printf("%c",aux[j]);
   					 par[e_3][j]=aux[j];
   				 }
   				 //printf("\n");
   				 ++e_3;
   			 }
   			 for(int j=0;j<e_2;++j){
   				 aux[j]=' ';
   			 }
   			 e_2=0;
   		 } else{
   			 aux[e_2]=inp[i];
   			 //printf("%c\n",inp[i]);
   			 u[0]=inp[i];
   			 ++e_2;
   		 }
   	 }
   	 for(int i=0;i<e_3;++i){
   		 for(int j=0;j<strlen(par[i]);++j){
                if((int)par[i][j]<48||(int)par[i][j]>57){
                    break;
                }
   			    printf("%c",par[i][j]);
   		 }
   		 printf(", ");
   	 }
     printf("sao valores divisiveis por dois");
   	 printf("\n");
   	 free(par);
   	 free(aux);
    }
    printf("Bye, bye!\n");
    return 0;
}