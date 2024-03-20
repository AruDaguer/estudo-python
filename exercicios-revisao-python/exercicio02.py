'''
Ex02 - Tabuada de Um Número: Solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.

'''

def tabuada(num):
    for multiplicador in range(1,11):
        resultado = multiplicador * num
        print(f'{num} X {multiplicador} = {resultado}')


num = int(input('Entre com um numero: '))
print(tabuada(num))

