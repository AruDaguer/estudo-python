'''
Ex03 - Contador de Vogais e Consoantes: Peça ao usuário para digitar uma frase e retorne o número de vogais e consoantes na frase.

'''

import unicodedata

frase = unicodedata.normalize('NFKD', input('Digite a frase: ').lower()).encode('ASCII', 'ignore').decode('ASCII')

vogais = 'aeiou'
consoantes = set(frase) - set(vogais)
cont_vogais = set(frase) - set(consoantes)

print(f'A frase tem {len(cont_vogais)} vogais')
print(f'A frase tem {len(consoantes)} consoantes')




    




