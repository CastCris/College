#include<stdio.h>
#include<stdlib.h>
//
void aumento(double ns[]){
    if(ns[0]<0||ns[0]>2500){
        ns[1]=0;
    } else if(ns[0]<=400){
        ns[1]=0.15;
    } else if(ns[0]<=700){
        ns[1]=0.12;
    } else if(ns[0]<=1000){
        ns[1]=0.10;
    } else if(ns[0]<=1800){
        ns[1]=0.07;
    } else if(ns[0]<=2500){
        ns[1]=0.04;
    }
    ns[0]+=ns[0]*ns[1];
}
//
int main(){
    char*inp,*aux=(char*)malloc(200*sizeof(char)),**names,**e_names,*slot;
    int tam=0,e1,e2,e3,espaco,nao,e_tam,index;
    double **n_num,**e_num;
    for(;;){
        for(int i=0;i<200;++i){
            aux[i]=' ';
        }
        inp=(char*)malloc(1000*sizeof(char));
        fgets(inp,1000,stdin);
        nao=0;
        for(e1=0;inp[e1]!='\0';++e1){
            if((int)inp[e1]!=80&&(int)inp[e1]!=112&&(int)inp[e1]>31){
                nao=1;
            }
            if(nao==1&&e1>2){
                break;
            }
        }
        if(e1<2){
            break;
        }
        if(nao==0){
            printf("\n");
            for(int i=0;i<tam;++i){
                printf("%s <- %.2lfU$ || %.2lf %c+\n",names[i],n_num[i][0],n_num[i][1],'%');
            }
            printf("\n");
        } else{
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
                        e_num[e3][1]=0.0;
                        aumento(e_num[e3]);
                        // printf("%.2lf %.2lf\n",e_num[e3][0],e_num[e3][1]);
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
                    for(index=0;index<e_tam;++index){
                        nao=0;
                        for(e1=0;(int)names[i][e1]<123&&(int)names[i][e1]>64&&(int)e_names[index][e1]<123&&(int)e_names[index][e1]>64;++e1){
                            if((int)names[i][e1]!=(int)e_names[index][e1]){
                                nao=1;
                                break;
                            }
                        }
                        if(nao==0&&(int)names[i][e1]>123&&(int)names[i][e1]<64&&(int)e_names[index][e1]>123&&(int)e_names[index][e1]<64){
                            break;
                        }
                    }
                    e_num[e3]=(double*)malloc(2*sizeof(double));
                    if(nao==1){
                        for(e2=0;(int)names[i][e2]<123&&(int)names[i][e2]>64;++e2){}
                        e_names[e3]=(char*)malloc((e2+5)*sizeof(char));
                        e_names[e3]=names[i];
                        e_num[e3][0]=n_num[i][0];
                        e_num[e3][1]=n_num[i][1];
                        ++e3;
                    } else{
                        printf("%.2lf %.2lf\n",e_num[index-1][0],n_num[i][0]);
                        e_num[index-1][0]=n_num[i][0];
                        e_num[index-1][1]=n_num[i][1];
                    }
                }
                free(n_num);
                free(names);
            }
            tam=e3;
            n_num=(double**)malloc(tam*sizeof(double*));
            names=(char**)malloc(tam*sizeof(char*));
            for(int i=0;i<tam;++i){
                for(e2=0;(int)e_names[i][e2]<123&&(int)e_names[i][e2]>64;++e2){}
                names[i]=(char*)malloc((e2+5)*sizeof(char));
                names[i]=e_names[i];
                n_num[i]=(double*)malloc(2*sizeof(double));
                n_num[i][0]=e_num[i][0];
                n_num[i][1]=e_num[i][1];
            }
            free(e_num);
            free(e_names);
        }
        free(inp);
    }
    printf("\nSalarios dos %i funcionarios da empresa XYZ:\n",tam);
    for(int i=0;i<tam;++i){
        printf("%s <- %.2lfU$ || %.2lf %c\n",names[i],n_num[i][0],n_num[i][1],'%');
    }
    printf("\nBye,bye!\n");
    return 0;
}