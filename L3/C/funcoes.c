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
    int e_1=0,e_2=0,e_3=0,ascii;
    bool epaco=true;
    char*aux;
    for(int i=0;i<MAX_SIZE_STRING;++i){
        ascii=(int)txt[i];
        if(ascii<48||ascii>57){
            if(ascii!=32&&ascii!=45)
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
                    aux[j]='_';
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
    int quant=0,ascii;
    bool epaco=true;
    for(int i=0;i<MAX_SIZE_STRING;++i){
        ascii=(int)texto[i];
        if(ascii==32&&!epaco){
            ++quant;
            epaco=true;
        } else if(ascii<32||ascii>126){
            break;
        } else if(ascii>32&&ascii<126){
            epaco=false;
        }
    }
    return quant+1;
}
//
void merge(int lista[],int inicio,int mind,int fim){
    int aux1,aux2,index=inicio,im=mind-inicio+1,me=fim-mind,i_m[im],m_e[me];
    for(int i=0;i<im;++i){
        i_m[i]=lista[inicio+i];
    }
    for(int i=0;i<me;++i){
        m_e[i]=lista[mind+i+1];
    }
    aux1=0;
    aux2=0;
    while(aux1<im&&aux2<me){
        if(i_m[aux1]<=m_e[aux2]){
            lista[index]=i_m[aux1];
            ++aux1;
        } else{
            lista[index]=m_e[aux2];
            ++aux2;
        }
        ++index;
    }
    for(aux1;aux1<im;++aux1){
        lista[index]=i_m[aux1];
        ++index;
    }
    for(aux2;aux2<me;++aux2){
        lista[index]=m_e[aux2];
        ++index;
    }
}
//
void merge_sort(int array[],int init,int end){
    if(init<end){
        int meio=init+(end-init)/2;
        merge_sort(array,init,meio);
        merge_sort(array,meio+1,end);
        merge(array,init,meio,end);
    }
}