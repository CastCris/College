#include<stdio.h>
#include<string.h>
#include<stdbool.h>
#include<stdlib.h>
//
int main(){
    bool ctrl;
    float v[2];
    char*inp,*split;
    printf("Insira dois valores para descobrir a distancia entre eles\n");
    for(;;){
        inp=(char*)malloc(100*sizeof(*inp));
        printf("*: ");
        fgets(inp,100,stdin);
        ctrl=true;
        for(int i=0;split=strtok_r(inp," ",&inp);++i){
            (int)split[0]>46&&(int)split[0]<58?ctrl=false:ctrl;
            v[i]=atof(split);
        }
        if(ctrl){
            break;
        }
        if (v[0]>v[1]){
            printf("%.2f\n",v[0]-v[1]);
        }else{
            printf("%.2f\n",v[1]-v[0]);
        }
    }
    printf("Bye, bye!");
    return 0;
}
