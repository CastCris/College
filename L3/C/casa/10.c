#include<stdio.h>
#include"../funcoes.h"
#include<stdlib.h>
//
void main(){
    char*inp,*aux,*slot;
    double*n,*temp;
    int e;
    printf("\nInsira uma expressao\n\n");
    for(;;){
        inp=(char*)malloc(1000*sizeof(char));
        printf("-> ");
        fgets(inp,1000,stdin);
        if(inp[0]=='S')
            break;
        n=(double*)calloc(1,sizeof(*n));
        aux=(char*)malloc(200*sizeof(*aux));
        for(int i=0;i<200;++i){
            if((int)inp[i]<48||(int)inp[i]>57)
                break;
            aux[i]=inp[i];
            ++e;
        }
        *n=strtod(aux,&slot);
        for(int i=0;i<e;++i){
            aux[i]=' ';
        }
        e=0;
        free(aux);
        for(int i=0;i<1000;++i){
            if(inp[i]=='+'||inp[i]=='-'||inp[i]=='*'||inp[i]=='/'){
                aux=(char*)malloc(200*sizeof(*aux));
                for(int j=0;j<200;++j){
                    if((int)inp[i+j+1]<47||(int)inp[i+j+1]>57)
                        break;
                    aux[j]=inp[i+j+1];
                }
                temp=(double*)malloc(1*sizeof(*temp));
                *temp=strtod(aux,&slot);
                if(inp[i]=='+'){
                    *n+=*temp;
                } else if(inp[i]=='-'){
                    *n-=*temp;
                } else if(inp[i]=='*'){
                    *n*=*temp;
                } else if(inp[i]=='/'){
                    *n/=*temp;
                }
                free(aux);
                free(temp);
            } else if((int)inp[i]<48||(int)inp[i]>58)
                break;
        }
        printf("%.0lf\n\n",*n);
        free(n);
        free(inp);
    }
    printf("Bye,bye!\n\n");
}