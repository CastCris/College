#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include"../funcoes.h"
//
void main(){
    char*inp;
    int*v;
    for(;;){
        inp=(char*)malloc(1000*sizeof(*inp));
        v=(int*)malloc(termos(inp)*sizeof(*v));
        fgets(inp,1000,stdin);
        string_to_int(inp,v);
        free(inp);
        //bubble ou merge?
        free(v);
    }
}