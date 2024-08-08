x=list(map(float,input('Insira as notas do aluno: ').split()))
v=0
for i in x:
    v+=i/len(x)
print("Reprovado",end='. ') if v<6 else print('Aprovado',end='. ')
print('Independentemente, a sua nota foi {:.2f}'.format(v))