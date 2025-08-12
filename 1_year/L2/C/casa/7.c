#include<stdio.h>
#include<string.h>
#include<stdlib.h>
//
int main(){
    char*inp=(char*)malloc(3*sizeof(*inp)),*out=(char*)malloc(20*sizeof(*out));
    printf("\nInsira o numero do curso: ");
    scanf("%s",inp);
    if(strcmp(inp,"1")==0)
        out="Engenharia";
    else if(strcmp(inp,"2")==0)
        out="Edificações";
    else if(strcmp(inp,"3")==0)
        out="Sistemas Elétricos";
    else if(strcmp(inp,"4")==0)
        out="Turismo";
    else if(strcmp(inp,"5")==0)
        out="Analise de Sistemas";
    else 
        out="Curso invalido";
    printf("%s\n\n",out);
    return 0;
}