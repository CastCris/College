#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<stdbool.h>
#include"../funcoes.h"
//
int main(){
    char*inp,*split;
    int*v,**receba;
    double*tot;
    bool  ctrl;
    for(;;){
        inp=(char*)malloc(1000*sizeof(char));
        v=(int*)calloc(4,sizeof(*v));
        fgets(inp,1000,stdin);
        for(int i=0;split=strtok_r(inp," ",&inp);++i){
            ctrl=true;
            if((int)split[0]>47&&(int)split[0]<58){
                ctrl=false;
            }
            v[i]=atoi(split);
        }
        if(ctrl)
            break;
        receba=(int**)malloc(2*sizeof(int*));
        looop(v,receba,0);
        tot=(double*)calloc(1,sizeof(double));
        for(int i=0;i<(v[1]-v[0])/v[2]+1;++i){
            if(receba[0][i]==0&&i>1){
                if(receba[0][i-1]>0)
                    break;
            }
            *tot+=receba[0][i];
        }
        printf("%.0lf\n",*tot);
    }
    return 0;
}