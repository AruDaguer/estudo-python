# for, while, (break/continue)

for letra in 'Olá Mundo' :
    print(letra)

prontuarios = ['SP01', 'SP02', 'SP03']

for prontuario in prontuarios:
    print(prontuario)

# range(5) => 0, 1, 2, 3, 4
for i in range(5):
    print(i)

# range(start, stop, step)
for i in range(0, 12, 2):
    print(i)

lista = list(range(1, 101))
print(lista)

# break 

comando = ''
while True:
    comando = input('Digite um comando: ')

    if comando == 'sair':
        break
    if comando == '1':
        print('1')
    if comando == '2':
        print('2')

#continue 
numeros = [3, -1, 2, 5, 6, 7]
for numero in numeros:
    if numero <= 0:
        continue
    print(numero)

for numero in numeros:
    if numero > 0:
        print(numero)

# compreensão de listas
numeros = [3, -1, 0, -5, 6, 7]

for numero in numeros:
    if numero > 0:
        positivos.append(numero)

positivos = [numero for numeros in numeros if numero > 0]
elevado_quad = [numero**2 for numero in numeros]

