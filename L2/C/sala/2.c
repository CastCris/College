#include<stdio.h>
#include<stdlib.h>
#include<string.h>
//
int main(){
	float v=0.0;
	char*inp=(char*)malloc(10*sizeof(*inp)),*split;
	printf("Insira as notas do aluno(uma linha): ");
	fgets(inp,10,stdin);
	for(int i=0;split=strtok_r(inp," ",&inp);++i){
		v+=atof(split)/2.0;
	}
	free(inp);
	if(v<6.0){
		char*sit=(char*)malloc(10*sizeof(*sit)),*inp=(char*)malloc(3*sizeof(*inp));
		sit="Aprovado!";
		printf("Isso nao e bom, faca o exame(fez o exame).\nAgora insira a nota do exame: ");
		fgets(inp,10,stdin);
		v+=atof(inp);
		v<5?sit="Reprovado!":sit;
		printf("%s",sit);
	} else {
		printf("Parabens!Te vejo no proximo bimestre!\n");
	}
	printf("Independe da sua condicao, voce tirou %.2f\n",v);
	free(inp);
	return 0;
}
