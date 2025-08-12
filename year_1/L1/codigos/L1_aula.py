#1
"""
x=list(map(float,input("Insira o tempo gasto e a velocidade média, respectivamente(uma linha): ").split()))
print('Velocidade média: '+str(x[1])+'KM/H\nTempo gasto: '+str(x[0])+'H\nDistância percorrida: '+str(x[0]*x[1])+'KM\nLitros utilizados: '+str(f'{(x[0]*x[1])/12:.2f}')+'L')
"""

#2
"""
print(str(f'{((float(input())-32)*5)/9:.1f}')+'°C')
"""

#3
"""
import math
x=float(input('RAIO: '))**2*float(input('ALTURA: '))*math.pi
print('Volume: '+f'{x:.2f}')
"""

#4
"""
x=[input() for _ in range(2)]
aux=x[0]
x[0]=x[1]
x[1]=aux
for _ in x: 
    print(_,end=' ')
"""

#5
"""
print("O quadrado misterioso vale:",f'{float(input("Insira um número para ser elevado a dois: "))**2:.0f}')
"""

#6
"""
v=float(input('VALOR(R$):'))
print('{:.2f}R$'.format(v+(v*(float(input('TAXA:'))/100)*float(input('TEMPO:')))))
"""

#7
"""
print('{:.2f}R$'.format((int(input('COELHOS:'))*0.7)/18+10))
"""