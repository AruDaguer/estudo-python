# 1. número 

# int 
idade = 20

# float
altura = 1.6

# complex
# calculos com números complexos
numero_complexo = 1 + 2j

# 2.boolean 
verdade = True
falso = False

# sequencias 
# String, lista, tuple, set, dict

# str 
# conjunto de caracter
nome = "Joao da Silva"

# str de multiplas linhas 
frase = """
Olá Mundo 
Parabéns
"""

# interpolação de str
nome = "Maria"
idade = 78
mensagem = f'{nome} é uma pessoa legal! Ela tem {idade} anos.'

# char 
# não existe 
# str tamanho 1

letra = 'A'

# Acessar caracter em strinf 
nome = 'Silvio Santos'
print(nome[2]) # >>> 1

# Métodos str

print(nome.upper())
print(nome.lower())

# list 
# lista de valores 
# permitir diferentes tipos de dados na mesma lista 

habilidades = ['python', 'java', 1]

print(habilidades[1]) # >>> java

for habilidade in habilidades:
    print(habilidade)

# adiciona no final da lista 
habilidades.append('html')

# adiciona na posição da lista 
habilidades.insert(1, 'css')

# remover 
habilidades.remove('css')

# tupla 
# "lista" de valores
# não pode ser alterada 
opcoes = ['sim', 'não', 'talvez'] # lista
opcoes = ('sim', 'não', 'talvez') # tupla


def estatistica_notas(notas) :
    maior = max(notas)
    menor = min(notas)
    media = sum(notas) / len(notas)
    return maior, menor, media

notas = [10, 8, 7, 8]
est = estatistica_notas(notas)
print(est)

# set 
# conjunto de valores 
# não é indexado 
# permite elementos duplicados 
habilidades = {'java', 'python'}

# dict 
# palavra -> definição 
# chave -> valor 
# key -> value 

nome = "Silvio"
idade = 89 
patrimonio = 2000000000
altura = 1.7

pessoa = {
    'nome' : 'Silvio',
    'idade' : 89,
    'patrimonio' : 2000000000,
    'altura' : 1.7
}

# None 
# variaveis que serão inicializadas em tempo de execução
# retorno de função 
# parametros de função
nulo = none 