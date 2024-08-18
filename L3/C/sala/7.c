#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include"../funcoes.h"
//
int main(void){
    char*inp;
    int*v,**receba,pot;
    for(;;){
        inp=(char*)malloc(1000*sizeof(char));
        v=(int*)calloc(4,sizeof(int));
        receba=(int**)malloc(2*sizeof(int*));
        fgets(inp,1000,stdin);
        string_to_int(inp,v);
        if(v[0]==0)
            break;
        pot=v[0];
        for(int i=0;i<4;++i){
            v[i]=v[i+1];
        }
        looop(v,receba,0);
        for(int i=0;i<(v[1]-v[0])/v[2]+1;++i){
            if(receba[0][i]==0&&i>1){
                if(receba[0][i-1]>0)
                    break;
            }
            printf("%i^%i = %0.lf\n",pot,receba[0][i],pow((double)pot,(double)receba[0][i]));
        }
        printf("\n");
        free(inp);
        free(v);
        free(receba);
    }
}