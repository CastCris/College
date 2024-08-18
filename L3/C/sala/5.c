#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include"../funcoes.h"
//
int main(){
    char*inp;
    int*v,**receba;
    for(;;){
        inp=(char*)malloc(1000*sizeof(char));
        fgets(inp,1000,stdin);
        v=(int*)calloc(4,sizeof(int));
        receba=(int**)malloc(2*sizeof(int*));
        string_to_int(inp,v);
        if(v[0]==0)
            break;
        looop(v,receba,0);
        for(int i=0;i<(v[1]-v[0])/v[2]+1;++i){
            if(receba[0][i]==0&&i>0){
                if(receba[0][i-1]>0)
                    break;
            }
            printf("%i ",receba[0][i]);
        }
        printf("\n");
        free(inp);
    }
}