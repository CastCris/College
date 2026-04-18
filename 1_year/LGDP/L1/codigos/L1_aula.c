#include <stdio.h>
#include <stdlib.h>
#include <math.h>
// 
int main(){
    double *x=(double*)calloc(3,sizeof(double));
    // 1
    /*<==
    //
    printf("Tempo: ");
    scanf("%lf",&x[0]);
    printf("Velocidade media: ");
    scanf("%lf",&x[1]);
    // 
    printf("Velocidade media %0.lf KM/H\nTempo gasto: %0.lf H\nDistacia percorrida: %.0lf KM\nLitros utilizados %.2lf L\n",x[1],x[0],x[1]*x[0],(x[1]*x[0])/12);
    ==>*/

    //2
    /*<==
    printf("Temperatura(F): ");
    scanf("%lf",&x[0]);
    printf("%.2lf C\n",(x[0]-32)*5/9);
    ==>*/

    //3
    /*<===
    printf("Raio: ");
    scanf("%lf",&x[0]);
    printf("Altura: ");
    scanf("%lf",&x[1]);
    printf("%.2lf\n",pow(x[0],2)*M_PI*x[1]);
    ===>*/

    //4
    /*
    char**inp=(char**)malloc(2*sizeof(char*)),*aux=(char*)malloc(100*sizeof(char));
    for(int i=0;i<2;++i){
        inp[i]=(char*)malloc(100*sizeof(char));
        printf("Variavel %c: ",(char)i+65);
        fgets(inp[i],100,stdin);
    }
    aux=inp[0];
    inp[0]=inp[1];
    inp[1]=aux;
    printf("%s%s",inp[0],inp[1]);
    free(inp);
    free(aux);
    */

    //5
    /*
    printf("Numero: ");
    scanf("%lf",&x[0]);
    printf("O seu quadrado: %.2lf\n",pow(x[0],2));
    */

    //6
    /*
    for(int i=0;i<3;++i){
        char *textinho=(char*)malloc(10*sizeof(char));
        i<1 ? textinho= "Valor": i<2?textinho= "Taxa" : i<3? textinho= "Tempo" : textinho;
        printf("%s: ",textinho);
        scanf("%lf",&x[i]);
    }
    printf("Valor a se pagar: %.2lf\n",x[0]+(x[0]*(x[1]/100.0)*x[2]));
    */

    //7
    /*
    printf("Quantidade de coelhos: ");
    scanf("%lf",&x[0]);
    printf("Custo de criacao: %.2lf R$\n",(x[0]*0.7)/18+10);
    */
    free(x);
    return 0;
}