## operadores aritméticos
## +, -, *, /< %, **

nota1 = 10.00
nota2 = 6.50
media = (nota1 + nota2) / 2

# 2 elevado ao quadrado 
potencia1 = 2 ** 2

# 2 elevado ao cubo 
potencia2 = 2 ** 3

# operadores de atribuição
# =, +=, -= ...

idade = 20 
idade += 10

# operadores lógicos 
# and, or, not 

# and           or
# 1 1 = 1       1 1 = 1 
# 1 0 = 0       1 0 = 1 
# 0 1 = 0       0 1 = 1 
# 0 0 = 0       0 0 = 0 

# operadores de comparação
# ==, =!, >, <, >=, <= 

idade = 17

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

# operador is
# os valores do objeto e se ocupam o mesmo
# espaço de memória

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b) # FALSE

c = [1, 2, 3]
x = c
print(c is x) # TRUE

# operador in e not in 
# verificar se o objeto esta ou não em uma sequência

print('a' in 'Java')
print('Maria' in ['Pedro', 'Ana'])

