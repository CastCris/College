while True:
        x=input('Insira os valores: ').split(' ')
        if(x[0]==''): break
        ok=False
        for i in x:
            if int(i[len(i)-1])%2==0:
                print(i,end=' ')
                ok=True
        if ok:
            print('\n')
print("Até!")