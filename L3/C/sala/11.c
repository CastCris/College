#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include"../funcoes.h"
//
void main(){
    char*inp;
    int*v,tam;
    for(;;){
        inp=(char*)malloc(1000*sizeof(*inp));
        fgets(inp,1000,stdin);
        tam=termos(inp);
        v=(int*)calloc(tam-1,sizeof(*v));
        string_to_int(inp,v);
        if(v[0]==0)
            break;
        free(inp);
        merge_sort(v,0,tam-1);
        for(int i=0;i<tam;++i){
            printf("%i ",v[i]);
        }
        printf("\n");
        free(v);
    }
}