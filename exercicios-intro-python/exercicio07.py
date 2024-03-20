'''
Ex07. Utilizando as diretrizes de Índice de Massa Corporal (IMC) da Organização Mundial de Saúde (OMS), crie uma calculadora em Python que solicita ao usuário seu peso (Kg) e sua altura (m) e apresenta em qual classificação o indivíduo se encaixa. Além disso, o programa deve apresentar quanto o indivíduo precisa perder ou ganhar de peso para chegar no peso normal (imc = 24,9).

IMC = peso / altura * altura

Classificação
----------------------------------
IMC           Classificação
-----------------------------------
< 18,5         Baixo peso
18,5 a 24,9     Peso normal
25,0 a 29,9     Excesso de peso
30,0 a 34,9     Obesidade de Classe 1
35,0 a 39,9     Obesidade de Classe 2
>= 40,00      Obesidade de Classe 3

Utilize funções.

'''

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Baixo peso"
    elif 18.5 <= imc < 25.0:
        return "Peso normal"
    elif 25.0 <= imc < 30.0:
        return "Excesso de peso"
    elif 30.0 <= imc < 35.0:
        return "Obesidade de Classe 1"
    elif 35.0 <= imc < 40.0:
        return "Obesidade de Classe 2"
    else:
        return "Obesidade de Classe 3"

def peso_ideal(altura):
    return 24.9 * (altura ** 2)

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)
peso_ideal_imc = peso_ideal(altura)

if imc < 18.5:
    necessidade_peso = peso_ideal_imc - peso
    mensagem = f'Você precisa ganhar {necessidade_peso} kg para atingir o peso normal.'
elif imc >= 25.0:
    necessidade_peso = peso - peso_ideal_imc
    mensagem = f'Você precisa perder {necessidade_peso} kg para atingir o peso normal.'
else:
    mensagem = 'Seu peso está dentro da faixa considerada normal.'

print(f'Seu IMC é: {imc}')
print(f'Classificação: {classificacao}')
print(mensagem)