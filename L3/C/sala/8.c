#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "../funcoes.h"
//
int main(){
    char*inp;
    int*v;
    double*fibo;
    printf("\nInsira um indice de fibonacci\n\n");
    for(;;){
        inp=(char*)malloc(1000*sizeof(char));
        v=(int*)calloc(1,sizeof(int));
        printf("-> ");
        fgets(inp,1000,stdin);
        string_to_int(inp,v);
        if(*v==0){
            break;
        }
        fibo=(double*)calloc(3,sizeof(double));
        fibo[1]=1;
        for(int i=0;i<*v;++i){
            printf("%.0lf ",fibo[1]);
            fibo[2]=fibo[1]+fibo[0];
            fibo[0]=fibo[1];
            fibo[1]=fibo[2];
        }
        printf("\n\n");
        free(v);
        free(fibo);
    }
    printf("Bye, bye!\n\n");
}