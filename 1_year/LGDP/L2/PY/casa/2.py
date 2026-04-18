print()
while True:
    x=list(map(float,input('Insira dois valores: ').split()))
    if len(x)<1:
        break
    v=x[1]-x[0]
    v*=-1 if v<0 else 1
    print('A diferença entre os valores é: {:.2f}'.format(v))
print('Até!\n')