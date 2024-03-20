'''

Ex06. Crie um programa em Python que recebe como entrada o comprimento, altura e a largura de um aquário e calcule as seguintes informações.

    O volume do aquário em litros;
    A potência do termostato necessária para manter a temperatura adequada dentro do aquário;
    A quantidade em litros de filtragem por hora necessária para manter a qualidade da água.

    Volume é dado por (comprimento * altura * largura) / 1000
    A potência do termostato depende do tamanho do aquário e da temperatura ambiente. Para o cálculo utilizar a fórmula: potencia = volume * 0,05 * (temperatura desejada - temperatura ambiente)
    A quantidade de filtragem por hora deve ser no mínimo 2 a 3 vezes o volume do aquário.

Utilize funções.


'''

def calcular_volume(comp, altura, largura):
    return (comp * altura * largura) / 1000

def calcular_potencia(volume, temperatura_desejada, temperatura_ambiente):
    return volume * 0.05 * (temperatura_desejada - temperatura_ambiente)

def calcular_filtragem(volume):
    return 2 * volume


comprimento = float(input("Entre com o omprimento do aquário (cm): "))
altura = float(input("Entre com a altura do aquário (cm): "))
largura = float(input("Entre com a largura do aquário (cm): "))
temperatura_desejada = float(input("Temperatura desejada (C): "))
temperatura_ambiente = float(input("Temperatura ambiente (C): "))

volume = calcular_volume(comprimento, altura, largura)
potencia_termostato = calcular_potencia(volume, temperatura_desejada, temperatura_ambiente)
filtragem = calcular_filtragem(volume)

print(f'Volume do aquário: {volume} litros')
print(f'Potência do termostato necessária: {potencia_termostato} ')
print(f'Quantidade de filtragem por hora necessária: {filtragem} litros por hora')

