'''
Ex03 - Contador de Vogais e Consoantes: Peça ao usuário para digitar uma frase e retorne o número de vogais e consoantes na frase.

'''

import unicodedata

frase = unicodedata.normalize('NFKD', input('Digite a frase: ').lower()).encode('ASCII', 'ignore').decode('ASCII')

vogais = 'aeiou'
consoantes = 0
cont_vogais = 0

for i in frase:
    if i in vogais:
        cont_vogais += 1
    elif i.isalpha():
        consoantes += 1

print(f'A frase tem {cont_vogais} vogais')
print(f'A frase tem {consoantes} consoantes')




    




