while True:
    x=list(map(int,input().split()))
    if len(x)<1:
        break
    if x[0]<=x[1]/5:
        while x[0]<x[1]:
            print(x[0])
            x[0]*=x[2]