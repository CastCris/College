while True:
    x=list(map(float,input('Insira n valores: ').split()))
    if len(x)<1:
        break
    x.sort()
    print('Organização decresente-> ',end=' ')
    for i in x:
        print('{:.2f}'.format(i),end=' ')
    print('\n')
print('Até!')