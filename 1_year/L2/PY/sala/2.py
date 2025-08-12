print()
x=list(map(float,input('Insira as notas: ').split()))
if (x[0]+x[1])/2>=6:
    print('Aprovado! A sua nota foi: {:.2f}'.format((x[0]+x[1])/2))
else:
    x.append(float(input('Insira a nota do exame: ')))
    print('Aprovado por exame') if (x[0]+x[1]+x[2])/3>=5 else print('Reprovado de qualquer jeito')
    print('Ainda assim, a sua nota foi {:.2f}'.format((x[0]+x[1]+x[2])/3))
print()