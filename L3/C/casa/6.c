#include<stdio.h>
#include<stdlib.h>
#include"../funcoes.h"
//
void main(){
    char*inp;
    int*v,**receba;
    printf("\nDescricao\n1-Valor x\n2-Valor y\n3-Valor z\n4-Valor a\nOutput esperado: duas sequencias de numeros multiplos e nao multiplos de a entre x e y a passo z\n\n");
    for(;;){
        inp=(char*)malloc(1000*sizeof(*inp));
        printf("-> ");
        fgets(inp,1000,stdin);
        if(termos(inp)==1)
            break;
        v=(int*)calloc(4,sizeof(int));
        string_to_int(inp,v);
        receba=(int**)malloc(2*sizeof(int*));
        free(inp);
        looop(v,receba,0);
        for(int i=0;i<2;++i){
            printf("Numeros");
            if(i==1)
                printf(" nao");
            printf(" divisiveis por %i: ",v[3]);
            for(int j=0;j<(v[1]-v[0])/v[2]+1;++j){
                if(receba[i][j]==0&&receba[i][j+1]==0)
                    break;
                printf("%i ",receba[i][j]);
            }
            printf("\n");
        }
        printf("\n");
        free(v);
        free(receba);
    }
    printf("Bye, bye!\n\n");
}