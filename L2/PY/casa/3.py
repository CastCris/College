while True:
    x=list(map(float,input('Insira as notas dos alunos: ').split()))
    if len(x)<1:
        break
    for i in x:
        print("{:.0f},0".format(i),end=' ')
    print('\n')
print('Até!')