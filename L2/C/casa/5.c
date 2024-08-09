#include<stdio.h>
#include<stdlib.h>
#include<string.h>
//
int main(){
    char*inp,*split;
    float v[2],novo;
    for(int f=0;;++f){
        printf("Insira os dados do %i funcionario: ",f);
        char*inp=(char*)malloc(1000*sizeof(char));
        fgets(inp,1000,stdin);
        if(inp[0]=='0'){
            break;
        }
        for(int i=0;split=strtok_r(inp," ",&inp);++i){
            v[i]=atof(split);
        }
        novo=v[0];
        1600>=novo&&novo>=800?novo-=(novo*0.13):novo>1600?novo-=(novo*0.22):novo;
        v[1]>160?novo+=(v[1]-160.0)*(0.5*(novo/160.0)):novo;
        printf("O seu salario sera: %.2fR$\n",novo);
    }
    printf("Verificacao check!\n");
}