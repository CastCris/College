#include<stdio.h>
#include<string.h>
#include<stdbool.h>
#include<stdlib.h>
#include"../funcoes.h"
//
int main(){
    int*v,**receba,m;
    char*inp,*split;
    bool ctrl;
    printf("\nDescricao:\n1-Valor n que sera mostrado a sua tabuada, situada na faixa entre y e z\n2-Valor y\n3-Valor z\n4-Passo\n\n");
    for(;;){
        inp=(char*)malloc(1000*sizeof(*inp));
        v=(int*)calloc(4,sizeof(*v));
        receba=(int**)malloc(2*sizeof(int*));
        printf("-> ");
        fgets(inp,100,stdin);
        for(int i=0;split=strtok_r(inp," ",&inp);++i){
            ctrl=true;
            i==0?m=atoi(split):i>0?v[i-1]=atoi(split):m;
            (int)split[0]>47&&(int)split[0]<58||split[0]=='-'?ctrl=false:ctrl;
            if(ctrl)
                break;
        }
        if(ctrl)
            break;
        printf("%i %i\n",v[0],v[1]);
        looop(v,receba,0);
        for(int i=0;i<(v[1]-v[0])/v[2]+1;++i){
            printf("%i*%i = %.0lf\n",m,receba[0][i],(double)m*receba[0][i]);
        }
        printf("\n");
        free(inp);
        free(v);
        free(receba);
    }
    printf("Bye, bye!\n\n");
    return 0;
}