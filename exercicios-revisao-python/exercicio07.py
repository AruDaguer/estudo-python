'''
Ex07 - Jogo da Forca: Implemente uma versão simples do jogo da forca. O programa começa com uma palavra oculta (o usuário não vê) 
e o usuário tenta adivinhar a palavra, letra por letra. O usuário tem um número limitado de tentativas para adivinhar toda a palavra.

'''

import random

# TENTATIVA PADRÃO
tentativas = 6

# DICIONARIOS
cores = {
    1: "azul",
    2: "vermelho",
    3: "verde",
    4: "amarelo",
    5: "roxo"
}

palavras_animais = {
    1: "cachorro",
    2: "elefante",
    3: "girafa",
    4: "tigre",
    5: "zebra"
}

palavras_objetos = {
    1: "computador",
    2: "cadeira",
    3: "mesa",
    4: "livro",
    5: "caneca"
}

# FUNÇÕES
def desenhar_boneco(tentativas):
    if tentativas == 6:
        print("  ________     ")
        print(" |/      |     ")
        print(" |             ")
        print(" |             ")
        print(" |             ")
        print(" |             ")
        print("_|___          ")
    elif tentativas == 5:
        print("  ________     ")
        print(" |/      |     ")
        print(" |      (_)    ")
        print(" |             ")
        print(" |             ")
        print(" |             ")
        print("_|___          ")
    elif tentativas == 4:
        print("  ________     ")
        print(" |/      |     ")
        print(" |      (_)    ")
        print(" |      \      ")
        print(" |             ")
        print(" |             ")
        print("_|___          ")
    elif tentativas == 3:
        print("  ________     ")
        print(" |/      |     ")
        print(" |      (_)    ")
        print(" |      \|    ")
        print(" |             ")
        print(" |             ")
        print("_|___          ")
    elif tentativas == 2:
        print("  ________     ")
        print(" |/      |     ")
        print(" |      (_)    ")
        print(" |      \|/    ")
        print(" |             ")
        print(" |             ")
        print("_|___          ")
    elif tentativas == 1:
        print("  ________     ")
        print(" |/      |     ")
        print(" |      (_)    ")
        print(" |      \|/    ")
        print(" |       |     ")
        print(" |             ")
        print("_|___          ")
    else:
        print("  ________     ")
        print(" |/      |     ")
        print(" |      (_)    ")
        print(" |      \|/    ")
        print(" |       |     ")
        print(" |      /      ")
        print("_|___   \\    ")

def palavra_aleatoria(tema):
    if tema == 1:
        palavra_secreta = random.choice(list(palavras_animais.values()))
    elif tema == 2:
        palavra_secreta = random.choice(list(palavras_objetos.values()))
    elif tema == 3:
        palavra_secreta = random.choice(list(cores.values()))
    return palavra_secreta

def jogo_da_forca(palavra_secreta, tentativas):
    palavra_oculta = ['_'] * len(palavra_secreta)
    letras_erradas = []
    
    print("Bem-vindo ao Jogo da Forca!")
    print("A palavra tem", len(palavra_secreta), "letras.")
    print(" ".join(palavra_oculta))
    
    while tentativas > 0 and '_' in palavra_oculta:
        letra = input("Digite uma letra: ").lower()
        
        if letra in palavra_secreta:
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    palavra_oculta[i] = letra
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            
        desenhar_boneco(tentativas)
        print("Palavra: ", " ".join(palavra_oculta))
        print("Letras erradas:", " ".join(letras_erradas))
        print("Tentativas que faltam:", tentativas)
        
    if '_' not in palavra_oculta:
        print("Você venceu!")
    else:
        print("Você perdeu! A palavra era:", palavra_secreta)


# RUN
print("Escolha um tema:")
print("1 - Animais")
print("2 - Objetos")
print("3 - Cores")
tema = int(input("Digite o número correspondente ao tema desejado: "))

palavra_secreta = palavra_aleatoria(tema)
jogo_da_forca(palavra_secreta, tentativas)

