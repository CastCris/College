print('\nInsira a ordem')
while True:
    if len(x:=list(map(int,input(': ').split())))<1:
        break
    print('Menor valor: {} | maior valor: {} da ordem acima\n'.format(min(x),max(x)))
print('Até!\n')