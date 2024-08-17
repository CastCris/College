while len(x:=input())>0:
    op,n='',int(x[0])
    for i in range(2,len(x)):
        op=x[i-1]
        if op=='*':
            n*=float(x[i])
        elif op=='+':
            n+=float(x[i])
        elif op=='-':
            n-=float(x[i])
        elif op=='/':
            n/=float(x[i])
    print(n)