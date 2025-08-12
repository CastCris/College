print('\nDescrição:\n1-Número que será analisado a sua tabuada\n2-Primeiro valor da sequência\n3-Último valor da sequência\n4-Passo\n')
while True:
    x=list(map(int,input(': ').split()))
    if len(x)<1:
        break
    mudar=False
    if x[1]>x[2]:
        x[1]-=x[2]
        x[2]+=x[1]
        x[1]=x[2]-x[1]
        mudar=True
    temp=x[1] if not mudar else x[2]
    print()
    for i in range(x[1],x[2]+1,x[3]):
        print('{}*{} = {}'.format(x[0],temp,x[0]*temp))
        temp+=x[3] if mudar==False else -x[3]
    print()
print('Até!\n')