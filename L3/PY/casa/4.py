while len(x:=list(map(int,input().split())))>0:
    mudar=False
    if x[0]>x[1]:
        x[0],x[1]=x[1],x[0]
        mudar=True
    temp=x[1] if mudar else x[0]
    for i in range(x[0],x[1]+1,x[2]):
        print(temp,end=' ')
        temp+=x[2] if not mudar else -x[2]
    print()