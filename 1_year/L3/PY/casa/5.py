print('\nDescrição:\n1-Valor y\n2-Valor z\n3-Passo\n4-Valor n para exibir todos os números de y a z não divisíveis por n\n')
while len(x:=list(map(int,input(': ').split())))>1:
    mudar=False
    if x[0]>x[1]: 
        x[0],x[1]=x[1],x[0]
        mudar=True
    temp=x[0] if not mudar else x[1]
    for i in range(x[0],x[1]+1,x[2]):
        print(temp,end=' ') if temp%x[3] else 0
        temp+=x[2] if not mudar else -x[2]
    print('\n')
print('Adeus!\n')