#include<stdio.h>
#include<string.h>
#include<stdbool.h>
#include<stdlib.h>
#include"../funcoes.h"
//
int main(){
    char*inp,*split;
    int *v,**recebe;
    bool ctrl;
    printf("\nDescricao:\n1-Valor y da sequencia\n2-Valor z da sequencia\n3-Passo\n4-Um numero n usado para exibir todos os valores nao divisiveis por n entre y e z \n\n");
    for(;;){
        ctrl=true;
        printf("-> ");
        inp=(char*)malloc(1000*sizeof(*inp));
        v=(int*)calloc(4,sizeof(*v));
        recebe=(int**)malloc(2*sizeof(int*));
        fgets(inp,1000,stdin);
        for(int i=0;split=strtok_r(inp," ",&inp);++i){
            if((int)split[0]>47&&(int)split[0]<58){
                ctrl=false;
            }
            v[i]=atoi(split);
        }
        if(ctrl){
            break;
        }
        looop(v,recebe,0);
        for(int i=0;i<(v[1]-v[0])/v[2]+1;++i){
            if(recebe[1][i]==0&&i>0&&recebe[1][i+1]==0){
                break;
            }
            printf("%i ",recebe[1][i]);
        }
        printf("\n\n");
        free(v);
        free(recebe);
    }
    printf("Bye bye!\n\n");
}