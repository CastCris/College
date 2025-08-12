#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<stdbool.h>
// 
int main(){
    float n=0.0;
    char*inp,*split;
    bool ctrl;
    for(;;){
        ctrl=true;
        inp=(char*)malloc(2*sizeof(inp));
        printf("\nInsira as notas do aluno(uma linha): ");
        fgets(inp,10,stdin);
        for(int i=0;split=strtok_r(inp," ",&inp);++i){
            if((int)split[0]>47&&(int)split[0]<58){
                ctrl=false;
            }
            n+=atof(split)/3.0;
        }
        if(ctrl){
            break;
        }
        if(n<6.0){
            printf("Reprovado(ao som do seu Madruga)! ");
        } else{
            printf("Aprovado! ");
        }
        printf("\nIndependente da sua condicao, voce tirou %.2f\n\n",n);
        free(inp);
        n=0;
    }
    printf("Bye, bye!\n\n");
    return 0;
}