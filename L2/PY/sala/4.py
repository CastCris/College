x=list(map(float,input('Insira o valor dos lados do triângulo: ').split()))
v=0
out='Escaleno'
rep=0
tri=True
for i in range(3):
    for j in range(3):
        v+=x[j] if j!=i else 0
        rep+=1 if x[i]==x[j] and j!=i else 0
    tri=x[i]<=v
    if tri==False:
        break
    v=0
if tri:
    if rep==2:
        out='Isósceles'
    elif rep==6:
        out='Equilátero'
    print(out)
else:
    print('Isso não é um triângulo')