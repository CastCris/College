#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// 
int main(){
    float n=0.0;
    char*inp=(char*)malloc(2*sizeof(inp)),*split;
    printf("Insira as notas do aluno(uma linha): ");
    fgets(inp,10,stdin);
    for(int i=0;split=strtok_r(inp," ",&inp);++i){
        n+=atof(split)/3.0;
    }
    if(n<6.0){
        printf("Reprovado(ao som do seu Madruga)! ");
    } else{
        printf("Aprovado! ");
    }
    printf("Independente da sua condicao, voce tirou %.2f",n);
    return 0;
}