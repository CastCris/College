print('\nDescrição:\n1-Valor y\n2-Valor z\n3-Passo\n4-Valor n para exibir todos os números de y a z divisíveis por n\n')
while len(x:=list(map(int,input().split())))>0:
    mudar=False
    if x[0]>x[1]:
        x[0],x[1]=x[1],x[0]
        mudar = True
    temp=x[0]
    temp=x[1] if mudar else temp
    while x[0]<x[1]+1:
        print(temp,end=' ') if temp%x[3]==0 else 0
        temp+=x[2] if mudar==False else 0
        temp-=x[2] if mudar else 0
        x[0]+=x[2]
    print('\n')
print('Adeus!\n')