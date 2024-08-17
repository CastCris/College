while True:
    x=list(map(int,input().split()))
    if len(x)<1:
        break
    mudar=False
    if x[1]>x[2]:
        x[1]-=x[2]
        x[2]+=x[1]
        x[1]=x[2]-x[1]
        mudar=True
    temp=x[1]
    print()
    for i in range(x[1],x[2]+1,x[3]):
        print('{}*{} = {}'.format(x[0],temp,x[0]*temp))
        temp+=x[3] if mudar==False else temp
        temp=x[2]-i if mudar else temp
    print()