print()
while True:
    x=list(map(float,input('Insira uma equação do 2º grau: ').split()))
    if len(x)<1:
        break
    if (x[1]**2)-(4*x[0]*x[2])<0:
        print('A equação não possui resolução')
    else:
        d=(x[1]**2)-(4*x[0]*x[2])
        print('Resposta=[ {:.2f} ; {:.2f} ]'.format((-x[1]+(d**0.5))/(2*x[0]),(-x[1]-(d**0.5))/(2*x[0])))
print('Até!\n')
