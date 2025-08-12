#include<stdio.h>
#include<stdlib.h>
//
int main(){
    printf("\n");
    char*inp,*aux=(char*)malloc(200*sizeof(char)),*prin=(char*)malloc(50*sizeof(char));
    int e1,e2,e3,*v,**faixas,pose;
    double*matrix;
    for(;;){
        inp=(char*)malloc(1000*sizeof(char));
        fgets(inp,1000,stdin);
        e2=0;
        for(e1=0;inp[e1]!='\0';++e1){
            if((int)inp[e1]==32){
                ++e2;
            }
        }
        if(e1<2){
            break;
        }
        v=(int*)malloc(e2*sizeof(int));
        for(int i=0;i<200;++i){
            aux[i]=' ';
        }
        for(e1=0,e2=0,e3=0;inp[e1]!='\0';++e1){
            if((int)inp[e1]==' '||inp[e1+1]=='\0'){
                inp[e1+1]=='\0'?aux[e3+1]=inp[e1]:aux[e3+1];
                v[e2]=atoi(aux);
                for(int i=0;i<e3+1;++i){
                    aux[i]=' ';
                }
                e3=0;
                ++e2;
            } else{
                aux[e3]=inp[e1];
                ++e3;
            }
        }
        matrix=(double*)calloc(10,sizeof(double));
        faixas=(int**)malloc(7*sizeof(int*));
        matrix[1]=matrix[2]=v[0];
        for(int i=0;i<e2;++i){
            matrix[0]+=(double)v[i]/e2;
            matrix[1]<v[i]?matrix[1]=v[i]:matrix[1];
            matrix[2]>v[i]?matrix[2]=v[i]:matrix[2];
            v[i]<0?pose=3:v[i]>=0&&v[i]<15?pose=4:v[i]>=15&&v[i]<100?pose=5:v[i]>=1000?pose=6:v[i]>=100&&v[i]<1000?pose=7:v[i];
            ++matrix[pose];
            v[i]%2?pose=8:v[i]%2==0?pose=9:v[i];
            ++matrix[pose];
        }
        for(int i=3;i<10;++i){faixas[i-3]=(int*)malloc(matrix[i]*sizeof(int));matrix[i]=0;}
        for(int i=0;i<e2;++i){
            v[i]<0?pose=3:v[i]>=0&&v[i]<15?pose=4:v[i]<100&&v[i]>=15?pose=5:v[i]>=1000?pose=6:v[i]>=100&&v[i]<1000?pose=7:v[i];
            faixas[pose-3][(int)matrix[pose]]=v[i];
            ++matrix[pose];
            v[i]%2?pose=8:v[i]%2==0?pose=9:v[i];
            faixas[pose-3][(int)matrix[pose]]=v[i];
            ++matrix[pose];
        }
        for(int i=0;i<10;++i){
            if(i==0){
                printf("Media aritimetica: %.2lf\n",matrix[0]);
            } else if(i==1){
                printf("Maior valor: %.0lf\n",matrix[1]);
            } else if(i==2){
                printf("Menor valor: %.0lf\n",matrix[2]);
            } else if(i>2&&i<8){
                printf("Faixa %i||Tamanho: %.0lf: ",i-2,matrix[i]);
                for(int j=0;j<matrix[i];++j){
                    printf("%i ",faixas[i-3][j]);
                }
                printf("\n");
            } else if(i==8){
                printf("Numeros impares||Tamanho: %.0lf: ",matrix[i]);
                for(int j=0;j<matrix[i];++j){
                    printf("%i ",faixas[i-3][j]);
                }
                if(matrix[i]>0){
                    printf("\n");
                }
            } else{
                printf("Numeros pares||Tamanho: %.0lf: ",matrix[i]);
                for(int j=0;j<matrix[i];++j){
                    printf("%i ",faixas[i-3][j]);
                }
                if(matrix[i]>0){
                    printf("\n");
                }
            }
        }
        printf("\n");
        free(v);
        free(matrix);
        free(faixas);
    }
    printf("Bye,bye!\n\n");
}