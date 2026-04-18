#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include"../funcoes.h"
//
void main(){
    char*inp;
    int*v,**receba;
    double*sum;
    printf("\nDescricao\n1-Primeiro valor do somatorio\n2-Ultimo valor do somatorio\n3-Passo\n4-Divisor\n\n");
    for(;;){
        receba=(int**)malloc(2*sizeof(*receba));
        inp=(char*)malloc(1000*sizeof(char));
        v=(int*)calloc(4,sizeof(int));
        printf("-> ");
        fgets(inp,1000,stdin);
        string_to_int(inp,v);
        free(inp);
        if(v[0]==0){
            break;
        }
        looop(v,receba,0);
        sum=(double*)calloc(1,sizeof(*sum));
        for(int i=0;i<(v[1]-v[0])/v[2]+1;++i){
            if(receba[0][i]==0&&i>1&&receba[0][i+1]==0){
                break;
            }
            *sum+=receba[0][i];
        }
        printf("%.0lf\n\n",*sum);
        free(v);
        free(receba);
        free(sum);
    }
    printf("Bye,bye!\n\n");
}