#include<stdio.h>
#include<string.h>
#include<stdbool.h>
#include<stdlib.h>
#include"../funcoes.h"
//
int main(){
    char*inp;
    int*v;
    for(;;){
        inp=(char*)malloc(1000*sizeof(*inp));
        v=(int*)calloc(3,sizeof(int));
        fgets(inp,1000,stdin);
        string_to_int(inp,v);
        if(v[1]==0)
            break;
        if(v[0]<=v[1]/5){
            for(;v[0]<v[1];){
                printf("%i ",v[0]);
                v[0]*=v[2];
            }
            printf("\n");
        }
        free(inp);
    } 
}