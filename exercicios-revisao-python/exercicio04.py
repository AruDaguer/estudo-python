'''
Ex04 - Simulador de Eleições: Crie um programa que simule uma votação com três candidatos.
O programa deve pedir ao usuário para votar várias vezes e, no final, mostrar o número de votos de cada candidato e quem foi o vencedor. 

'''

candidatos = {
    1: "Candidato1",
    2: "Candidato2",
    3: "Candidato3"
}

votos = {}
for i in candidatos:
    votos[i] = 0

num = int(input("Quantos votos deseja simular? "))

for _ in range(num):
    print('Para Candidato1: VOTE 1')
    print('Para Candidato2: VOTE 2')
    print('Para Candidato3: VOTE 3')
    voto = int(input('VOTE: '))

    if voto in votos:
        votos[voto] += 1
    else:
        print("Não existe esse candidato")

vencedor = max(votos)

print(f'O vencedor é o {candidatos[vencedor]} com {votos[vencedor]} votos.')


