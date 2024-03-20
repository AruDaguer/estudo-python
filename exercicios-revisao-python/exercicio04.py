'''
Ex04 - Simulador de Eleições: Crie um programa que simule uma votação com três candidatos.
O programa deve pedir ao usuário para votar várias vezes e, no final, mostrar o número de votos de cada candidato e quem foi o vencedor. 

'''

candidato1 = 1
candidato2 = 2
candidato3 = 3
cont1 = 0
cont2 = 0
cont3 = 0

for i in range(11):
    print('Para Candidato1: VOTE 1')
    print('Para Candidato2: VOTE 2')
    print('Para Candidato3: VOTE 3')
    voto = int(input('VOTE: '))

    if voto == 1:
        cont1 += 1
    elif voto == 2:
        cont2 += 1
    elif voto == 3:
        cont3 += 1

if cont1 > cont2 and cont1 > cont3:
    vencedor = candidato1
elif cont2 > cont1 and cont2 > cont3:
    vencedor = candidato2
elif cont3 > cont1 and cont3 > cont2:
    vencedor = candidato3

print(f'Canditato{vencedor} ganhou')


