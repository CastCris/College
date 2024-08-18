#include"funcoes.h"
#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>
//
void looop(int valores[], int**nm, int op){
    int divi=1,q=0,*temp,e[2]={0,0};
    bool mudar=false;
    for(int i=0;i<4;++i){
        if(valores[i]==0&&i>1)
            break;
        ++q;
    }
    if(q==4)
        divi=valores[3];
    else if(q>4||q<2)
        return;
    if(q<3)
        valores[2]=1;
    if(valores[0]>valores[1]){
        valores[0]-=valores[1];
        valores[1]+=valores[0];
        valores[0]=valores[1]-valores[0];
        mudar=true;
    }
    temp=(int*)calloc(1,sizeof(*temp));
    mudar?*temp=valores[1]:!mudar?*temp=valores[0]:*temp;
    for(int i=0;i<2;++i){
        nm[i]=(int*)calloc((valores[1]-valores[0])/valores[2],sizeof(int));
    }
    for(int i=valores[0];i<valores[1]+1;i+=valores[2]){
        if(*temp%divi){
            nm[1][e[1]]=*temp;
            ++e[1];
        } else{
            nm[0][e[0]]=*temp;
            ++e[0];
        }
        mudar?*temp-=valores[2]:!mudar?*temp+=valores[2]:*temp;
    }
};
//
void string_to_int(char txt[],int conjunto[]){
    int e_1=0,e_2=0,e_3=0;
    bool epaco=true;
    char*aux;
    for(int i=0;i<MAX_SIZE_STRING;++i){
        if((int)txt[i]<48||(int)txt[i]>57){
            if((int)txt[i]!=32)
                break;
        }
        ++e_1;
    }
    txt[e_1]=' ';
    aux=(char*)malloc(e_1*sizeof(char));
    for(int i=0;i<e_1+1;++i){
        if((int)txt[i]==32){
            if(!epaco){
                epaco=true;
                conjunto[e_3]=atoi(aux);
                for(int j=0;j<e_2;++j){
                    aux[j]=' ';
                }
                e_2=0;
                ++e_3;
            }
        } else{
            epaco=false;
            aux[e_2]=txt[i];
            ++e_2;
        }
    }
}
//
int termos(char*texto){
    int quant=0;
    for(int i=0;i<MAX_SIZE_STRING;++i){
        if((int)texto[i]==32){
            ++quant;
        } else if((int)texto[i]<32||(int)texto[i]>126){
            break;
        }
    }
    return quant+1;
}