i=0
while True:
    print("Insira os dados do {} funcionário: ".format(i),end=' ')
    x=list(map(float,input().split()))
    if x[0]==0:break
    x[0]-=(x[0]*0.13) if x[0]>=800 and x[0]<=1600 else 0
    x[0]-=(x[0]*0.22) if x[0]>1600 else 0
    x[0]+=(x[1]-160)*(0.5*(x[0]/160)) if x[1]>160 else 0
    print("O seu salário será {:.2f}R$".format(x[0]))
    i+=1
print('Até!')