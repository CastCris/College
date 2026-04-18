print('\nDescrição:\n1-Valor y da sequência\n2-Valor z da sequência\n3-Passo\n4-Um número n usado para exibir todos os valores não divisíveis por n entre y e z \n')
while True:
    x=list(map(int,input(': ').split()))
    if len(x)<1:
        print()
        break
    mudar=False
    print("Números não divisíveis por {} de {} até {}:".format(x[3],x[0],x[1]))
    if x[0]>x[1]:
        x[0],x[1]=x[1],x[0]
        mudar=True
    temp=x[0] if not mudar else x[1]
    for i in range(x[0],x[1],x[2]):
        temp+=x[2] if not mudar else -x[2]
        print(temp,end=' ') if temp%x[3] else ''
    print('\n')
print("Até!\n")