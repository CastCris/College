print()
x=list(map(float,input('Itens a serem organizados: ').split()))
x.sort()
for i in x:
    print(i,end=' ')
print('\n')
