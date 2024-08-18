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
    for(;;){
        inp=(char*)malloc(1000*sizeof(*inp));
        v=(int*)calloc(4,sizeof(*v));
        receba=(int**)malloc(2*sizeof(int*));
        fgets(inp,100,stdin);
        for(int i=0;split=strtok_r(inp," ",&inp);++i){
            ctrl=true;
            i==0?m=atoi(split):i>0?v[i-1]=atoi(split):m;
            (int)split[0]>47&&(int)split[0]<58?ctrl=false:ctrl;
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
    }
    return 0;
}