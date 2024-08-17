while True:
    if len(x:=list(map(int,input().split())))<1:
        break
    print(max(x),min(x))