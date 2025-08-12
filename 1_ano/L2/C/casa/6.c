#include<stdio.h>
#include<string.h>
#include<stdlib.h>
//
int main(){
    char bgl[3],*out=(char*)malloc(20*sizeof(*out)),*inp=(char*)malloc(3*sizeof(*inp));
    printf("\nInsira um mes: ");
    scanf("%s",inp);
    if(strcmp(inp,"1")==0)
        out="Janeiro";
    else if(strcmp(inp,"2")==0)
        out="Fevereiro";
    else if(strcmp(inp,"3")==0)
        out="Marco";
    else if(strcmp(inp,"4")==0)
        out="Abril";
    else if(strcmp(inp,"5")==0)
        out="Maio";
    else if(strcmp(inp,"6")==0)
        out="Junho";
    else if(strcmp(inp,"7")==0)
        out="Julho";
    else if(strcmp(inp,"8")==0)
        out="Agosto";
    else if(strcmp(inp,"9")==0)
        out="Setembro";
    else if(strcmp(inp,"10")==0)
        out="Outubro";
    else if(strcmp(inp,"11")==0)
        out="Novembro";
    else if(strcmp(inp,"12")==0)
        out="Dezembro";
    else
        out="Invalido";
    printf("%s\n\n",out);
    return 0;
}