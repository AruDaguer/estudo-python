# ifentificadores
# letras, numeros e _
# não pode ser palavras reservadas: if, None, True...
# case sensitive
nome = "Pedro"
Nome = "Pedro"

# variáveis
# tudo em minúsculo
# separador _
# snake_case
idade = 20
pessoa_fisica = "Marcio"
pessoa_juridica = "Paula"
imposto_renda = 2200.45

# tipo 
# python inferência de tipo 
# tipo definido no valor literal
idade = 20 #int
nome = "Pedro" #str

# constante
# não existe constante
# convenção: nome em maiúsculo 
PI = 3.14

# comentário de única linha 

'''
comentário de
 multiplas linhas 
'''

# docstring (comentário de documentação)
# documentar classe, módulos, funções...

def somar(numero1, numero2) :
    '''
    soma dois números
    '''
    return numero1 + numero2

somar #documentação