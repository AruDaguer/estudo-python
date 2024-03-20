'''
Ex01 - Jogo de Adivinhação: Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu aleatoriamente. 
Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número.

'''

import random

def jogo_adivinhacao(num):
    aleatorio = random.randint(1,100)

    while True:
        if num == aleatorio:
            print('ACERTOU!')
            break
        elif num > aleatorio:
            num = int(input('Entre com valor mais baixo: '))
        
        elif num < aleatorio:
            num = int(input('Entre com valor mais alto: '))

num = int(input('Entre com número aleatório (1,100): '))
jogo_adivinhacao(num)
    

