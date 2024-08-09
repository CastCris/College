#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<stdbool.h>
//
int main(){
    bool ctrl;
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
            printf("%.0f,0 ",atof(split));
        }
        if(ctrl){
            break;
        }
        printf("\n");
    }
    printf("Bye, bye!\n");
    return 0;
}