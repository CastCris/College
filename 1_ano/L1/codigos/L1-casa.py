import math
#1
"""
print("U$ {:.2f}".format(float(input("R$->U$: "))/2.4))
"""

#2
"""
print("R$ {:.2f}".format(float(input("U$->R$: "))*2.4))
"""

#3
"""
x=list(map(int,input("Insira o valor do comprimeto e largura da parede e do azulejo(uma linha): ").split()))
print("A parede suporta, confortavelmente, {:.0f} azulejos".format(((x[0]*x[1])/(x[2]*x[2]))))
"""

#4
"""
x=list(map(int,input("Insira a largura e o comprimento do retângulo(uma linha): ").split()))
print("O valor de sua área é: {}; e o seu perímetro é: {}".format((x[0]*x[1]),(x[0]*2+x[1]*2)))
"""

#5
"""
x=list(map(float,input("Insira a sua masa, kg, e a sua altura, m(uma linha): ").split()))
print("O seu IMC é: {:.2f}".format(x[0]/(x[1]**2)))
"""

#6
"""
x=float(input("Insira o raio da circunferência: "))
print("A área da cirunferência equivale à {:.2f} e o seu comprimento é {:.2f}".format((x**2)*math.pi,math.pi*2*x))
"""

#7
"""
x=float(input("Insira o raio da bola: "))
print("O volume da esfera é {:.2f}; e a área de sua superfície é {:.2f}".format((4/3)*math.pi*(x**3),4*math.pi*(x**2)))
"""

#8
"""
x=list(map(float,input("Insira as notas do aluno(uma linha): ").split()))
y=0
for i in x: y+=i
print("A média final, considerando as {} etapas anteriores e as regulamentações, o aluno X tirou {:.2f}".format(len(x),y/len(x)))
"""

#9
"""
x=list(map(float,input("Insira as notas das provas do semestre e das atividades(uma linha): ").split()))
print("Considerando as regulamentações, o aluno tirou {:.2f} no semestre".format((x[0]*4+x[1]*4+x[2]*2)/10))
"""

#10
"""
x=input("Insira as variaveis: ").split()
for i in range(0,int(len(x)/2),1):
    aux=x[i]
    x[i]=x[len(x)-i-1]
    x[len(x)-i-1]=aux
for i in x:
    print(i,end=' ')
"""

#11
"""
:/
"""

#12
"""
x=list(map(float,input("Insira a distância percorrida e o tempo gasto(em uma linha): ").split()))
print("A velocidade média foi {}KM/h".format(x[0]/x[1]))
"""

#13
"""
x=float(input("Insira um tempo, em segundos: "))
print("s = {}m".format(2+(3*x)+0.5*(10*(x**2))))
"""