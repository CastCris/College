print()
while True:
    if len(x:=list(map(float,input('Insira y e z(uma linha): ').split())))<1:
        break
    print('{}^{} = {:.0f}'.format(x[0],x[1],x[0]**x[1]))
    print()
print('Até!\n')