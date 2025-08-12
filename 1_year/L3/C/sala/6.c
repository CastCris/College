#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include"../funcoes.h"
//
int main(void){
    char*inp;
    int*v,**receba,pot;
    printf("\nDescricao:\n1-Valor n(potencia)\n2-Primeiro valor da sequencia\n3-Segundo valor da sequencia\n3-Passo\n\n");
    for(;;){
        receba=(int**)malloc(2*sizeof(int*));
        inp=(char*)malloc(1000*sizeof(char));
        v=(int*)calloc(4,sizeof(int));
        printf("-> ");
        fgets(inp,1000,stdin);
        string_to_int(inp,v);
        if(v[0]==0)
            break;
        pot=v[0];
        for(int i=0;i<4;++i){
            v[i]=v[i+1];
        }
        looop(v,receba,0);
        for(int i=0;i<(v[1]-v[0])/v[2]+1;++i){
            if(receba[0][i]==0&&i>0&&receba[0][i+1]==0)
                break;
            printf("%i^%i = %.0lf | ",receba[0][i],pot,pow((double)receba[0][i],(double)pot));
        }
        printf("\n\n");
        free(inp);
        free(v);
        free(receba);
    }
    printf("Bye, bye!\n\n");
}