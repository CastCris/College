#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<stdbool.h>
//
int main(){
    bool ctrl;
    printf("\n");
    float ponte;
    for(;;){
        printf("Insira as notas dos alunos: ");
        ctrl=true;
        char*inp=(char*)malloc(1000*sizeof(*inp)),*split;
        fgets(inp,1000,stdin);
        for(;split=strtok_r(inp," ",&inp);){
            (int)split[0]>46&&(int)split[0]<58?ctrl=false:ctrl;
            if(ctrl){
                break;
            }
            ponte=atof(split);
            if(ponte-(int)ponte<=0.5){
                printf("%i,0",(int)ponte);
            } else{
                printf("%i,0",(int)ponte+1);
            }
        }
        if(ctrl){
            break;
        }
        printf("\n");
    }
    printf("Bye, bye!\n\n");
    return 0;
}