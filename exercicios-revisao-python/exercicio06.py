'''
Ex06 - Conversor de Notas Escolares: Baseado em uma pontuação fornecida pelo usuário (0 a 100), 
converta para o sistema de notas A, B, C, D, ou F, seguindo os padrões de conversão comuns.

'''

def converter_nota(pontuacao):
    if pontuacao >= 90:
        return 'A'
    elif pontuacao >= 80:
        return 'B'
    elif pontuacao >= 70:
        return 'C'
    elif pontuacao >= 60:
        return 'D'
    else:
        return 'F'

pontuacao = int(input("Entre com sua pontuação (0 a 100): "))

nota = converter_nota(pontuacao)

print(f"A nota correspondente é: {nota}")
