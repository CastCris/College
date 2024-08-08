while True:
    x=list(map(float,input('Insira dois valores: ').split()))
    if len(x)<1:
        break
    v=x[1]-x[0]
    v=x[0]-x[1] if x[0]>x[1] else v
    print('A diferença entre os valores é: {:.2f}'.format(v))
print('Até!')