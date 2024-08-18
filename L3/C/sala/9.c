#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include"../funcoes.h"
//
int main(void){
    char*inp;
    int*v;
    for(;;){
        inp=(char*)malloc(1000*sizeof(char));
        v=(int*)calloc(2,sizeof(int));
        fgets(inp,1000,stdin);
        string_to_int(inp,v);
        if(v[0]==0)
            break;
        printf("%i^%i = %.0lf\n",v[0],v[1],pow((double)v[0],(double)v[1]));
        free(inp);
        free(v);
    }
}