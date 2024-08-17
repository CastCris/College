while len(x:=list(map(int,input().split())))>0:
    mudar=False
    if x[0]>x[1]:
        x[0],x[1]=x[1],x[0]
        mudar=True
    divi,temp=[[],[]],x[0]
    temp=x[1] if mudar else temp
    while x[0]<x[1]+1:
        divi[1].append(temp) if temp%x[3] else divi[0].append(temp)
        temp+=x[2] if not mudar else 0
        temp-=x[2] if mudar else 0
        x[0]+=x[2]
    for i in range(2):
        print('Números',end='')
        if i==1:
            print(' não',end='')
        print(' Divisíveis por {}: '.format(x[3]),end='')
        for j in divi[i]:
            print(j,end=' ')
        print()