while len(x:=list(map(int,input().split())))>0:
    mudar=False
    if x[0]>x[1]: 
        x[0],x[1]=x[1],x[0]
        mudar=True
    temp=x[0] if not mudar else x[1]
    for i in range(x[0],x[1]+1,x[2]):
        print(temp,end=' ') if temp%x[3] else 0
        temp+=x[2] if not mudar else -x[2]
    print()