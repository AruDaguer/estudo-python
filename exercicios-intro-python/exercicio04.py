"""

Ex04 - O código identificador de funcionários de uma empresa contém 7 caracteres, inicia com a sequência de caracteres BR, em seguida apresenta um número inteiro entre 0001 e 9999 e finaliza com o caractere X.

Exemplos válidos:

    BR0001X
    BR1236X
    BR9999X

Exemplos inválidos:

    br0001X
    BR126X
    BR99999X
    BR9999Y
    
Crie uma função em Python que implementa essa verificação

"""

def verificacao(codigo):
    if len(codigo) != 7:
        return False
    
    if codigo[:2] != "BR" or codigo[-1] != "X":
        return False
    
    numero = int(codigo[2:6])
    if numero < 1 or numero > 9999:
        return False
    
    return True
    



