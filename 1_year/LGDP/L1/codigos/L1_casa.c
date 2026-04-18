#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
//
int main(){
    double *x=(double*)calloc(4,sizeof(double));
    //1
    /*
    printf("R$: ");
    scanf("%lf",&x[0]);
    printf("%.2lfR$ = %.2lfU$\n",x[0],x[0]/2.4);
    */

    //2
    /*
    printf("U$: ");
    scanf("%lf",&x[0]);
    printf("%.2lfU$ = %.2lfR$",x[0],x[0]*2.4);
    */

    //3
    /*
    int e=0;
    for(int i=0;i<2;++i){
        char*txt=(char*)malloc(8*sizeof(char)),*inp=(char*)malloc(21*sizeof(char)),*store;
        i<1?txt="parede":i<2?txt="azulejo":txt;
        printf("Entre com o comprimento do %s e a sua largura (uma linha): ",txt);
        fgets(inp,10,stdin);
        char*split=strtok(inp," ");
        for(int j=0;split!=NULL;++j){
            x[e]=strtod(split,&store);
            split=strtok(NULL," ");
            ++e;
        }
    }
    printf("A parede posera ser comportar, confortavelmente, %.0lf azulejos",(x[0]*x[1])/(x[2]*x[3]));
    */

    //4
    /*
    printf("Entre com o comprimentos e largura, respectivamente, do retangulo(uma linha): ");
    char*entrada=(char*)malloc(10*sizeof(char)),*split;
    fgets(entrada,10,stdin);
    split=strtok(entrada," ");
    for(int i=0;split!=NULL;++i){
        char*armaze;
        x[i]=strtod(split,&armaze);
        split=strtok(NULL," ");
    }
    printf("A area do retangulo e: %.2lf e o seu perimetro e %.2lf",x[0]*x[1],x[0]*2.0+x[1]*2.0);
    free(entrada);
    */

    //5
    /*
    char*split,*store,*inp;
    inp=(char*)malloc(8*sizeof(char));
    printf("Insira a massa do individuo, kg, e a sua altura, em m,(uma linha): ");
    fgets(inp,100,stdin);
    split=strtok(inp," ");
    for(int i=0;split!=NULL;++i){
        x[i]=strtod(split,&store);
        split=strtok(NULL," ");
    }
    printf("O IMC do organismo e: %.2lfkg/m^2",x[0]/pow(x[1],2));
    */
    
    //6
    /*
    printf("Insira o raio do circulo: ");
    scanf("%lf",&x[0]);
    printf("O valor de sua area e %.2lf; E de sua circunferencia: %.2lf",pow(x[0],2)*M_PI, M_PI*2*x[0]);
    */
    
    //7
    /*
    printf("Insira o raio da bola: ");
    scanf("%lf",&x[0]);
    printf("O seu volume e %.2lf; Sua superfice equivale a %.2lf",4.0/3.0*M_PI*pow(x[0],3),4*M_PI*pow(x[0],2));
    */
    
    //8
    /*
    printf("Insira as notas do cidadao(em uma linha): ");
    double v=0.0,e=0.0;
    char*inp=(char*)malloc(20*sizeof(char)),*split,*armazenar;
    fgets(inp,20,stdin);
    split=strtok(inp," ");
    for(int i=0;split!=NULL;++i){
        v+=strtod(split,&armazenar);
        split=strtok(NULL," ");
        e+=1.0;
    }
    printf("A nota final do aluno, considerando que ambos os bimestres tem o mesmo peso, foi: %.2lf",v/e);
    */
    
    //9
    /*
    printf("Insira as notas do aluno: ");
    char*inp=(char*)malloc(20*sizeof(char)),*split,*armazenar;
    fgets(inp,20,stdin);
    for(int i=0;split=strtok_r(inp," ",&inp);++i){
        x[i]=strtod(split,&armazenar);
    }
    printf("A nota final do cidadao foi: %.2lf",(x[0]*4.0+x[1]*4.0+x[2]*3.0)/10.0);
    */
    
    //10
    /*
    printf("Insira os valores: ");
    char*inp=(char*)malloc(21*sizeof(char)),*split,**trem=(char**)malloc(2*sizeof(char*)),*aux=(char*)malloc(10*sizeof(char));
    fgets(inp,100,stdin);
    for(int i=0;split=strtok_r(inp," ",&inp);++i){
        trem[i]=(char*)malloc(10*sizeof(char));
        trem[i]=split;
    }
    aux=trem[0];
    trem[0]=trem[1];
    trem[1]=aux;
    printf("O valor trocadas variaveis e: %s %s",trem[0],trem[1]);
    free(inp);
    */
    //11
    /* :/ */
    
    //12
    /*
    printf("Insira o tempo, h, gasto e a distancia percorrida, km. Em uma linha: ");
    char*inp=(char*)malloc(15*sizeof(char)),*split,*armazenar;
    fgets(inp,100,stdin);
    for(int i=0;split=strtok_r(inp," ",&inp);++i){
        x[i]=strtod(split,&armazenar);
    }
    printf("A velocidade media foi: %.2lfKm/h",x[1]/x[0]);
    */
    
    //13
    /*
    printf("Insira os segundos: ");
    int t;
    scanf("%i",&t);
    printf("s = %.2lf,\n",2+(3*t)+0.5*(10*pow(t,2)));
    */
    free(x);
    return 0;
}