while True:
    x=input('Insira os valores: ').split()
    if len(x)<1:
        break
    men=False
    for i in x:
        su=0
        for j in i:
            su+=int(j)
        if su%3==0 and int(i[len(i)-1])%2==0:
            print(i,end=' ')
            men=True
    if men:
        print('são numeros divisiveis por 6')
print('Até!')