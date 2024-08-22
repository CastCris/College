print('\nDescrição:\n1-Valor y da sequência\n2-Valor z da sequência\n3-Passo\n4-Um número n usado para somar todos os valores divisíveis por n entre y e z\n')
while True:
    if len(x:=list(map(int,input().split())))<1:
        break
    elif x[0]>x[1]:
        x[0],x[1]=x[1],x[0]
    valor,repre=0,x[0]
    for i in range(x[0],x[1]+1,x[2]):
        valor+=i if i%x[3]==0 else 0
    print(valor,'\n')
print('Até!\n')