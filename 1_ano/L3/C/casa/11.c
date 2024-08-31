#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include"../funcoes.h"
//
void main(){
    char*inp;
    int*v,**receba,m;
    printf("\nDescricao\n1-Valor x\n2-Valor y\n3-Valor z\n4-Valor A\nOutput esperado: uma tabuada de x dos numeros y a z a passo A\n\n");
    for(;;){
        inp=(char*)malloc(1000*sizeof(*inp));
        printf("-> ");
        fgets(inp,1000,stdin);
        if(termos(inp)==1)
            break;
        v=(int*)malloc(termos(inp)*sizeof(*v));
        string_to_int(inp,v);
        m=v[0];
        for(int i=0;i<termos(inp);++i){
            v[i]=v[i+1];
        }
        free(inp);
        receba=(int**)malloc(2*sizeof(*receba));
        looop(v,receba,0);
        for(int i=0;i<(v[1]-v[0])/v[2]+1;++i){
            if(receba[0][i]==0&&receba[0][i+1]==0)
                break;
            printf("%i*%i = %0.lf\n",m,receba[0][i],(double)m*(double)receba[0][i]);
        }
        printf("\n\n");
    }
    printf("Bye, bye!\n\n");
}