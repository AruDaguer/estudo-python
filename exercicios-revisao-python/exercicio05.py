'''
Ex05 - Verificador de Palíndromos: Solicite ao usuário que digite uma palavra ou frase e 
verifique se é um palíndromo (ou seja, pode ser lida de frente para trás e de trás para frente da mesma forma).

'''

str = input('Entre com um palavra ou frase: ')
verificador = str[::-1]

if str == verificador:
    print('É palindromo')
else:
    print('Não é palindromo')