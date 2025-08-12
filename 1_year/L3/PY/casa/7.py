print('\nDescrição:\n1-Primeiro valor da sequência\n2-Último valor da sequência\n3-passo\n')
while len(x:=list(map(int,input(': ').split())))>1:
    mudar=False
    if x[0]>x[1]:
        x[0],x[1]=x[1],x[0]
        mudar=True
    temp=x[1] if mudar else x[0]
    while True:
        print(temp,end=' ')
        temp+=x[2] if not mudar else -x[2]
        x[0]+=x[2]
        if x[0]>x[1]:
            break
    print('\n')
print('Adeus!\n')