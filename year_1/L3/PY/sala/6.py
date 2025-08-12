print('\nDescrição:\n1-Valor y da sequência\n2-Valor z da sequência\n3-Passo\n4-Um número n usado para exibir todos os quadrados inteiros entre y e z\n')
while True:
    mudar=False
    if len(x:=list(map(int,input(': ').split())))<1:
        break
    elif x[0]>x[1]:
        x[0],x[1]=x[1],x[0]
        mudar=True
    temp=x[0] if mudar==False else temp
    temp=x[1] if mudar else temp
    for i in range(x[0],x[1]+1,x[2]):
        print('{}^{} = {} | '.format(temp,x[3],temp**x[3]),end=' ')
        temp+=x[2] if mudar==False else 0
        temp-=x[2] if mudar else 0
    print('\n')
print('Até!\n')