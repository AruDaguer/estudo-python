# Função
# modularizar o programa
# reuso
# manutenabilidade

# só pode acessar a hora se for entre 8h e 18h 
# horario comercial
hora_atual = 12

if hora_atual >= 8 and hora_atual <= 18:
    print('permitido o acesso')

# entrada = hora_atual
# saida se esta dentro ou nao do horario comercial

# junior
def dentro_horario_comercial(hora):
    if hora_atual >= 8 and hora_atual <= 18:
        return True
    else:
        return False

# pleno
def dentro_horario_comercial(hora):
    return hora_atual >= 8 and hora_atual <= 18

# seior 
dentro_horario_comercial = lambda hora_atual: hora_atual >= 8 and hora_atual <= 18

# Declaração
# def nome_funcao():
#     corpo da funcao

# Funcao sem retorno (pior)
# Side effect - efeito colateral 
def diga_ola(nome):
    print(f'Olá {nome}')

# Funcao com retorno (melhor)
# Sem side effect = funcao pura
def diga_ola(nome):
    return f'Olá {nome}'

print(diga_ola('Julio'))

# Chamada
diga_ola('Marcos')

# Parãmetro e Argumentos 
# Parâmetros são referências que podem ser acessadas dentro da funcao
# Argumento são os valores passados para os Parâmetros

def somar(numero1, numero2):
    return numero1 + numero2

somar(10, 4)

# Escopo de variáveis 
# variavel local 
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

# variavel global 
total = 0

def soma_tres(n1, n2, n3):
    # global total
    total = n1 + n2 + n3
    return total

print(total)
soma_tres(1, 4, 60)
print(total)

# Parâmetros com valor padrão 
def boas_vindas(mensagem='Bom dia', nome='Marcos'):
    return f'{mensagem}, {nome}'

print(boas_vindas('bom dia','marcos'))
print(boas_vindas(nome='Jucara'))

# Docstring 
# Comentário de documentação

def somar(numero1, numero2) :
    '''
    soma dois números
    '''
    return numero1 + numero2

print(somar(1,2))

# Funções Built-in
# print, type, len, sum, max, min, input
# ver no python3 interativo terminal




