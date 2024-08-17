while True:
    x=list(map(int,input().split()))
    if len(x)<1:
        break
    mudar=False
    if x[0]>x[1]:
        x[0]-=x[1]
        x[1]+=x[0]
        x[0]=x[1]-x[0]
        x[1]+=x[0]
        mudar=True
    temp=x[0]
    for i in range(x[0],x[1],x[2]):
        temp=x[1]-i if mudar else temp
        print(temp,end=' ') if temp%x[3] else 0
        temp+=x[2]
    print()