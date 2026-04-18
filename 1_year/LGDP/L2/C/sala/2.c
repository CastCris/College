#include<stdio.h>
#include<stdlib.h>
#include<string.h>
//
int main(){
	float v[2],n;
	char*inp=(char*)malloc(10*sizeof(*inp)),*split;
	printf("\nInsira as notas do aluno(uma linha): ");
	fgets(inp,10,stdin);
	for(int i=0;split=strtok_r(inp," ",&inp);++i){
		v[i]=atof(split);
	}
	free(inp);
	n=(v[1]+v[0])/2.0;
	if(n<6.0){
		char*sit=(char*)malloc(10*sizeof(*sit)),*inp=(char*)malloc(3*sizeof(*inp));
		sit="Aprovado!";
		printf("Isso nao e bom, faca o exame(fez o exame).\nAgora insira a nota do exame: ");
		fgets(inp,10,stdin);
		n=(v[0]+v[1]+atof(inp))/3.0;
		n<5.0?sit="Reprovado!":sit;
		printf("%s",sit);
	} else {
		printf("Parabens!Te vejo no proximo bimestre!\n");
	}
	printf("Independe da sua condicao, voce tirou %.2f\n\n",n);
	free(inp);
	return 0;
}