'''
Ex05 - Crie um programa em Python que solicita ao usuário um identificador e apresenta se o que foi informado é um valor válido ou inválido.

'''

from exercicio04 import verificacao

codigo = input('Entre com seu codigo: ')

if verificacao(codigo):
    print('VÁLIDO')
else:
    print('INVÁLIDO')

