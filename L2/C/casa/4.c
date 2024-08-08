#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>
//
int main(){
    printf("\n");
    bool ctrl;
    int q;
    float*v;
    char*inp,*split;
    for(;;){
        q=0;
        printf("Insira os valores a serem organizados: ");
        ctrl=true;
        inp=(char*)malloc(1000*sizeof(char));
        fgets(inp,1000,stdin);
        for(int i=0;i<1000;++i){
            if((int)inp[i]==32){
                ++q;
            } else if((int)inp[i]<46||(int)inp[i]>57){
                break;
            }
            ctrl=false;
        }
        if(ctrl){
            break;
        }
        ++q;
        v=(float*)calloc(q,sizeof(float));
        for(int i=0;split=strtok_r(inp," ",&inp);++i){
            v[i]=atof(split);
        }
        for(int i=0;i<q;++i){
            for(int j=0;j<q;++j){
                if(v[i]<v[j]){
                    v[i]+=v[j];
                    v[j]=v[i]-v[j];
                    v[i]-=v[j];
                }
            }
        }
        for(int i=0;i<q;++i){
            printf("%.2f ",v[i]);
        }
        printf(" e a sua forma mais organizada");
        printf("\n\n");
    }
    printf("Bye, bye!\n");
    return 0;
}
