print('\nDescrição:\n1-Valor n\n2-Primeiro valor da tabuada\n3-Último valor da tabuada\n4-Passo\n')
while len(x:=list(map(int,input(': ').split())))>0:
    mudar=True if x[1]>x[2] else False
    if mudar:x[1],x[2]=x[2],x[1]
    temp=x[2] if mudar else x[1]
    for i in range(x[1],x[2]+1,x[3]):
        print('{}*{} = {}'.format(x[0],temp,x[0]*temp))
        temp-=x[3] if mudar else -x[3]
    print('\n')
print('Adeus!\n')