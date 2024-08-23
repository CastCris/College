print('\nDescrição:\n1-Valor y\n2-Valor z\n3-Passo\n4-Valor n para exibir todos os números de y a z divisíveis por n\n')
while len(x:=list(map(int,input(': ').split())))>1:
    mudar=False
    if x[0]>x[1]:
        x[0],x[1]=x[1],x[0]
        mudar=True
    temp=x[1] if mudar else x[0]
    while True:
        print(temp,end=' ') if not temp%x[3] else 0
        temp+=x[2] if not mudar else -x[2]
        x[0]+=x[2]
        if x[0]>x[1]:break
    print('\n')
print('Adeus!\n')