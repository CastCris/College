#include<stdio.h>
#include<stdlib.h>
#include"../funcoes.h"
//
void main(){
    char*inp;
    int*v,**receba;
    for(;;){
        inp=(char*)malloc(1000*sizeof(*inp));
        fgets(inp,1000,stdin);
        if(termos(inp)==1)
            break;
        v=(int*)calloc(4,sizeof(*v));
        string_to_int(inp,v);
        free(inp);
        receba=(int**)malloc(2*sizeof(*receba));
        looop(v,receba,2);
        for(int i=0;i<2;++i){
            for(int j=0;j<(v[1]-v[0])/v[2]+1;++j){
                if(receba[i][j]==0&&receba[i][j+1]==0)
                    break;
                printf("%i ",receba[i][j]);
            }
            printf("\n");
        }
        free(v);
        free(receba);
    }
}