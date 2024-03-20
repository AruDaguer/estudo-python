# if, if/else, if,elif,else, ternario, match

# if
# if condição:
#     corpo
#     corpo
#     corpo  

idade = 20

if idade >= 18:
    print("Maior de idade")

print('Acabou o programa')

# if/else
if idade >= 18:
    print("Maior")
else:
    print("Menor")

# criança (0 - 12) adolescente (13 - 17) adulto (18 - 59) idoso (60+)

if idade <= 12:
    print("criança")
elif idade <= 17:
    print("adolescente")
elif idade <= 59:
    print("adulto")
else:
    print("idoso")

# operador ternário 
if idade >= 18:
    status = 'maior'
else:
    status = 'menor'

# usuário passa o dia (int)
# devolve string nome 
# 1 - domingo 2 - segunda ...
dia = 4

# dicionário 

dias = {
    1: 'Domingo',
    2: 'Segunda',
    3: 'Terça',
    4: 'Quarta',
    5: 'Quinta',
    6: 'Sexta',
    7: 'Sábado'
}

if dia in dias:
    print(dias[dia])

# match
# switch case mais poderoso

dia = 2
match dia:
    case 1:
        print('Domingo')
    case 2:
        print('Segunda')
    case 3:
        print('Terça')
    case 4:
        print('Quarta')
    case 5:
        print('Quinta')
    case 6:
        print('Sexta')
    case 7:
        print('Sábado')        

match dia:
    case 1 | 7:
        print('Final de semana')
    case 2 | 3 | 4 | 5 | 6:
        print('Dia de semana')
    case _:
        print('INVALIDO')

