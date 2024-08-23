#include<stdio.h>
#include<stdlib.h>
#include"../funcoes.h"
//
void main(){
    char*inp;
    int*v,**receba;
    printf("\nDescricao\n1-Valor x\n2-Valor y\n3-Valor z\n4-Valor a\nOutput esperado: uma sequencia de todos os numeros multiplos de a na sequencia de x a y a passo z\n\n");
    for(;;){
        inp=(char*)malloc(1000*sizeof(*inp));
        printf("-> ");
        fgets(inp,1000,stdin);
        if(termos(inp)==1)
            break;
        v=(int*)calloc(4,sizeof(*v));
        string_to_int(inp,v);
        free(inp);
        receba=(int**)malloc(2*sizeof(int*));
        looop(v,receba,1);
        for(int i=0;i<(v[1]-v[0])/v[2]+1;++i){
            if(receba[0][i]==0&&i>0&&receba[0][i+1]==0)
                break;
            printf("%i ",receba[0][i]);
        }
        printf("\n\n");
    }
    printf("Bye, bye!\n\n");
}