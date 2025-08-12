#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include"../funcoes.h"
//
void main(){
    char*inp;
    int*v,tam;
    printf("\nInsira a ordem\n\n");
    for(;;){
        inp=(char*)malloc(1000*sizeof(*inp));
        printf("-> ");
        fgets(inp,1000,stdin);
        tam=termos(inp);
        v=(int*)calloc(tam-1,sizeof(*v));
        string_to_int(inp,v);
        if(v[0]==0)
            break;
        free(inp);
        merge_sort(v,0,tam-1);
        printf("%i %i\n\n",v[0],v[tam-1]);
        free(v);
    }
    printf("Bye, bye!\n\n");
}