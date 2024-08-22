print('\nDescrição:\n1-Primeiro valor da sequência\n2-Último valor da sequência\n3-Passo\n4-Um número n usado para exibir todos os valores divisíveis por n na sequência\n')
while True:
    x=list(map(int,input(': ').split()))
    if len(x)<1:
        break
    mudar=False
    if x[0]>x[1]:
        x[0],x[1]=x[1],x[0]
        mudar=True
    temp=x[0]
    temp=x[1]+x[2] if mudar else temp
    for i in range(x[0],x[1],x[2]):
        temp+=x[2] if mudar==False else 0
        temp-=x[2] if mudar else 0
        print(temp,end=' ')if temp%x[3]==0 else 0
    print('\n')
print('Até!\n')