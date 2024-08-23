print('\nInsira n números e operações\nNota: a expresão não deve conter espações vazios\n*Essa calculadora não é indicada para uso científico ou de aplicação tecníca\n')
while len(x:=input(': '))>0:
    op,n='',int(x[0])
    for i in range(2,len(x)):
        op=x[i-1]
        if op=='+'or op=='-'or op=='*'or op=='/':
            nn=''
            for j in range(i,len(x)):
                try:
                    int(x[j])
                    nn+=x[j]
                except:
                    break
            if op=='*':
                n*=float(nn)
            elif op=='+':
                n+=float(nn)
            elif op=='-':
                n-=float(nn)
            elif op=='/':
                n/=float(nn)
            op=' '
    print(n,'\n')
print("Adeus!\n")