#include<stdio.h>
#include<stdlib.h>
#include"../funcoes.h"
//
void main(){
    char*inp;
    int*v,**receba;
    printf("\nDescricao\n1-Valor x\n2-Valor y\n3-Valor z\n4-Valor a\nOutput esperado: uma sequencia de todos os numeros nao multiplos de a na sequencia de x a y a passo z\n\n");
    for(;;){
        inp=(char*)malloc(1000*sizeof(*inp));
        printf("-> ");
        fgets(inp,1000,stdin);
        if(termos(inp)==1)
            break;
        v=(int*)calloc(4,sizeof(*v));
        string_to_int(inp,v);
        free(inp);
        receba=(int**)malloc(2*sizeof(*receba));
        looop(v,receba,0);
        for(int i=0;i<(v[1]-v[0])/v[2];++i){
            if(receba[1][i]==0&&receba[1][i+1]==0)
                break;
            printf("%i ",receba[1][i]);
        }
        free(v);
        free(receba);
        printf("\n\n");
    }
    printf("Bye, bye!\n\n");
}