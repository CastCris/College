print()
while True:
    x=input('Insira os valores: ').split()
    if len(x)<1:
        break
    ok=False
    for i in x:
        q=''
        q_r=''
        for j in range(3):
            if j>len(i)-1:
                break
            q+=i[len(i)-1-j]
        for j in range(len(q)):
            q_r+=q[len(q)-1-j]
        if int(q_r)%4==0 or int(i[len(i)-1])%5==0:
            print(i,end=' ')
            ok=True
    if ok:
        print('são números divisíveis por 4||5')
print('Até!\n')