print('\nDescrição:\n1-Valor x\n2-Primeiro valor da sequência\n3-Último valor da seuência\n4-Passo\n')
while True:
    mudar=False
    if len(x:=list(map(int,input().split())))==0:
        break
    elif x[1]>x[2]: 
        x[1],x[2]=x[2],x[1]
        mudar=True
    temp=x[1]
    temp=x[2] if mudar else temp
    for i in range(x[1],x[2]+1,x[3]):
        print('{}^{} = {}'.format(x[0],temp,x[0]**temp))
        temp+=x[3] if mudar==False else 0
        temp-=x[3] if mudar else 0
    print()
print('Até!\n')