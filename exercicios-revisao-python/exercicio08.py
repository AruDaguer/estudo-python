'''
Ex08 - Função de Contagem de Palavras: Escreva uma função que receba uma string (frase) como argumento 
e retorne um dicionário onde as chaves são as palavras únicas no texto e os valores são o número de vezes que cada palavra aparece no texto. 
Depois, teste a função com diferentes textos fornecidos pelo usuário. 

'''
import string

def contar_palavras(frase):
    contagem = {}
    
    frase = frase.translate(str.maketrans('', '', string.punctuation))
    
    palavras = frase.split()
    
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    
    return contagem

frase = input("Digite uma frase: ")
resultado = contar_palavras(frase)
print("Contagem de palavras:", resultado)