#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include"../funcoes.h"
//
int main(){
    char*inp;
    int*v,**receba;
    printf("\nDescricao:\n1-Valor i1\n2-Valor in\n3-Passo\n4-Um numero n usado para exibir todos os valores divisiveis por n entre os numeros i1 e in\n\n");
    for(;;){
        inp=(char*)malloc(1000*sizeof(char));
        printf("-> ");
        fgets(inp,1000,stdin);
        v=(int*)calloc(4,sizeof(int));
        receba=(int**)malloc(2*sizeof(int*));
        string_to_int(inp,v);
        if(v[0]==0)
            break;
        looop(v,receba,0);
        for(int i=0;i<(v[1]-v[0])/v[2]+1;++i){
            if(receba[0][i]==0&&i>0&&receba[0][i+1]==0)
                break;
            printf("%i ",receba[0][i]);
        }
        printf("\n\n");
        free(inp);
        free(v);
        free(receba);
    }
    printf("Bye, bye!\n\n");
}