#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "../funcoes.h"
//
int main(){
    char*inp;
    int*v,*fibo;
    for(;;){
        inp=(char*)malloc(1000*sizeof(char));
        v=(int*)calloc(1,sizeof(int));
        fgets(inp,1000,stdin);
        string_to_int(inp,v);
        if(*v==0){
            break;
        }
        fibo=(int*)calloc(3,sizeof(int));
        fibo[1]=1;
        for(int i=0;i<*v;++i){
            printf("%i ",fibo[1]);
            fibo[2]=fibo[1]+fibo[0];
            fibo[0]=fibo[1];
            fibo[1]=fibo[2];
        }
        printf("\n");
        free(v);
        free(fibo);
    }
}