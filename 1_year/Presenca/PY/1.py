print('\nPara cada vez que o loop se repetir, presione a tecla p para visualizar os funcionários\n')
funcionarios={}
def salario(n):
    valor=0 if n<=0 or n>2500 else 0.15
    valor-=0.03 if n>400 and valor!=0 else 0
    valor-=0.02 if n>700 and valor!=0 else 0
    valor-=0.03 if n>1000 and valor!=0 else 0
    valor-=0.03 if n>1800 and valor!=0 else 0
    return "{:.2f}$\n{:.2f}% de aumento\n".format(n+n*valor,valor)
while (x:=input('Insira um conjunto de funcionários: ').split()):
    if x[0]=='p':
        for i in funcionarios.keys():
            print(i,funcionarios[i])
    else:
        y=list(map(salario,list(map(float,input('Insira seus respectivos salários: ').split()))))
        for i in x:
            funcionarios[i]=y[0] if i not in funcionarios.keys() else funcionarios[i]
            y.pop(0)
for i in funcionarios:
    print('{}<- {}'.format(i,funcionarios[i]))
print()