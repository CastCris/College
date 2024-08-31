#include<stdio.h>
#include<stdlib.h>
//
void aumento(double n,double porcen){
    if(n<0||n>2500){
        return;
    } else if(n<=400){
        porcen=0.15;
    } else if(n<=700){
        porcen=0.12;
    } else if(n<=1000){
        porcen=0.10;
    } else if(n<=1800){
        porcen=0.07;
    } else if(n<=2500){
        porcen=0.04;
    }
    n+=n*porcen;
}
//
int main(){
    char*inp,*aux=(char*)malloc(200*sizeof(char)),**names,**e_names,*slot;
    int tam=0,e1,e2,e3,espaco,nao,e_tam;
    double **n_num,**e_num;
    for(;;){
        for(int i=0;i<200;++i){
            aux[i]=' ';
        }
        inp=(char*)malloc(1000*sizeof(char));
        fgets(inp,1000,stdin);
        for(e1=0,e3=1;inp[e1]!='\0';++e1){
            ((int)inp[e1]==32)?++e3:e3;
        }
        e_tam=e3;
        e_names=(char**)malloc((tam+e3)*sizeof(char*));
        for(e1=0,e2=0,e3=0;inp[e1]!='\0';++e1){
            if((int)inp[e1]==32||inp[e1+1]=='\0'){
                if(espaco==0){
                inp[e1+1]=='\0'?aux[e2+1]=inp[e1]:aux[e2];
                e_names[e3]=(char*)malloc((e2+10)*sizeof(char));
                for(int j=0;j<e2;++j){
                    e_names[e3][j]=aux[j];
                    aux[j]=' ';
                }
                ++e3;
                espaco=1;
                e2=0;
                }
            } else{
                aux[e2]=inp[e1];
                ++e2;
                espaco=0;
            }
        }
        for(int i=0;i<200;++i){
            aux[i]=' ';
        }
        fgets(inp,1000,stdin);
        e_num=(double**)malloc((tam+e3)*sizeof(double*));
        for(e1=0,e2=0,e3=0;inp[e1]!='\0';++e1){
            if((int)inp[e1]==32||inp[e1+1]=='\0'){
                if(espaco==0){
                    e_num[e3]=(double*)malloc(2*sizeof(double));   
                    inp[e1+1]=='\0'?aux[e2+1]=inp[e1]:aux[e2];
                    e_num[e3][0]=strtod(aux,&slot);
                    e_num[e3][1]=0;
                    
                    aumento(e_num[e3][0],e_num[e3][1]);
                    for(int j=0;j<e2;++j){
                        aux[j]=' ';
                    }
                    ++e3;
                    e2=0;
                    espaco=1;
                }
            } else{
                aux[e2]=inp[e1];
                ++e2;
                espaco=0;
            }
        }
        //
        if(tam>0){
            for(int i=0;i<tam;++i){
                for(int j=0;j<e_tam;++j){
                    nao=0;
                    for(e1=0;(int)names[i][e1]<123&&(int)names[i][e1]>64&&(int)e_names[j][e1]<123&&(int)e_names[j][e1]>64;++e1){
                        if((int)names[i][e1]!=(int)e_names[j][e1]){
                            nao=1;
                            break;
                        }
                    }
                    if(nao==0){
                        break;
                    }
                }
                if(nao==1){
                    for(e2=0;(int)names[i][e2]<123&&(int)names[i][e2]>64;++e2){}
                    e_names[e3]=(char*)malloc((e2+5)*sizeof(char));
                    e_names[e3]=names[i];
                    e_num[e3]=(double*)malloc(2*sizeof(double));
                    e_num[e3][0]=n_num[i][0];
                    e_num[e3][1]=n_num[i][1];
                    ++e3;
                }
            }
            free(n_num);
            free(names);
        }
        tam=e3;
        // printf("%i\n",tam);
        // for(int i=0;i<tam;++i){
        //     printf("%s-%.2lf\n",e_names[i],e_num[i]);
        // }
        n_num=(double**)malloc(tam*sizeof(double*));
        names=(char**)malloc(tam*sizeof(char*));
        for(int i=0;i<tam;++i){
            for(e2=0;(int)e_names[i][e2]<123&&(int)e_names[i][e2]>64;++e2){}
            names[i]=(char*)malloc((e2+5)*sizeof(char));
            names[i]=e_names[i];
            n_num=(double**)malloc(2*sizeof(double*));
            n_num[i][0]=e_num[i][0];
            n_num[i][1]=e_num[i][1];
        }
        for(int i=0;i<tam;++i){
            printf("%s %.2lf\n",names[i],n_num[i]);
        }
        free(inp);
        free(e_num);
        free(e_names);
    }
    return 0;
}