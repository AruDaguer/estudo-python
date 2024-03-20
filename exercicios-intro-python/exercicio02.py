'''
Ex02 - Escreva um programa em Python que solicita ao usuário três números e apresenta a média aritmética dos números informados.

'''

lista = [
    float(input('Entre com primeiro número: ')),
    float(input('Entre com segundo número: ')),
    float(input('Entre com terceiro número: '))
]

print(f'Média = {sum(lista) / len(lista)}')