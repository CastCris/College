print()
x=input()
match x:
    case '1':
        x='Janeiro'
    case '2':
        x='Faveiro'
    case '3':
        x='Março'
    case '4':
        x='Abril'
    case '5':
        x='Maio'
    case '6':
        x='Junho'
    case '7':
        x='Julho'
    case '8':
        x='Agosto'
    case '9':
        x='Setembro'
    case '10':
        x='Outubro'
    case '11':
        x='Novembro'
    case '12':
        x='Dezembro'
    case _:
        x='Mes inválido'
print(x,'\n')