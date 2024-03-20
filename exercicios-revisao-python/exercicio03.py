'''
Ex03 - Contador de Vogais e Consoantes: Peça ao usuário para digitar uma frase e retorne o número de vogais e consoantes na frase.

'''

import unicodedata

vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = [ 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'w', 'z']
frase = unicodedata.normalize('NFKD', input('Digite a frase: ').lower()).encode('ASCII', 'ignore').decode('ASCII')
cont = 0
cont1 = 0

for i in frase:
    if i in vogais:
        cont += 1

for j in frase:
    if j in consoantes:
        cont1 += 1

print(f'A frase tem {cont} vogais')
print(f'A frase tem {cont1} consoantes')




    




