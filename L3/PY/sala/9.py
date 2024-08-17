while True:
    if len(x:=list(map(float,input().split())))<1:
        break
    print(x[0]**x[1])