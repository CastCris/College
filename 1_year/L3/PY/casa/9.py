print('\nDescrição:\n1-Primeiro valor da sequência\n2-Último valor da sequência\n3-passo\n4-Número divisor\n')
while len(x:=list(map(int,input(': ').split())))>1:
    mudar=False
    if x[0]>x[1]:
        x[0],x[1]=x[1],x[0]
        mudar=True
    temp=x[1] if mudar else x[0]
    divi=[[],[]]
    while True:
        divi[0].append(temp) if not temp%x[3] else divi[1].append(temp)
        temp-=x[2] if mudar else -x[2]
        x[0]+=x[2]
        if x[0]>x[1]: break
    for i in range(2):
        print('Números',end='')
        if i==1: print(' não',end='')
        print(' divisíveis por {}: '.format(x[3]),end='')
        for j in divi[i]:
            print(j,end=' ');
        print()
    print('\n')
print('Adeus!\n')