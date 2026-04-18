print('\nDescrição:\n1-Número n\n2-Limite x de n\n3-Valor y que n será multiplicado sucesivamente enquanto for <x\n')
while True:
    x=list(map(int,input(': ').split()))
    if len(x)<1:
        break
    if x[0]<=x[1]/5:
        while x[0]<x[1]:
            print(x[0],end=' ')
            x[0]*=x[2]
        print('\n')
print('Até!\n')