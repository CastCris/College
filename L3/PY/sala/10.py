while True:
    if len(x:=list(map(int,input().split())))<1:
        break
    elif x[0]>x[1]:
        x[0],x[1]=x[1],x[0]
    valor,repre=0,x[0]
    for i in range(x[0],x[1]+1,x[2]):
        valor+=i if i%x[3]==0 else 0
    print(valor)