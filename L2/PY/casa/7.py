x=input('\n')
match x:
    case '1':
        x='Engenharia'
    case '2':
        x='Edificações'
    case '3':
        x='Sistemas Elétricos'
    case '4':
        x='Turismo'
    case '5':
        x='Análise de Sistemas'
    case _:
        x='Inválido'
print(x,'\n ')