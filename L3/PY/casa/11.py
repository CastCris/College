while len(x:=list(map(int,input().split())))>0:
    for i in range(x[1],x[2]+1,x[3]):
        print('{}*{} = {}'.format(x[0],i,x[0]*i))
    print()