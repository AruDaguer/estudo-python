# Crie um programa em Python que recebe como entrada o valor de uma 
# compra e apresenta como saída o valor final com desconto e o desconto aplicado com base nas seguintes regras:

# Compras entre R$ 0,01 e R$ 9,99 - 0% de desconto
# Compras entre R$ 10,00 e R$ 99,99 - 5% de desconto
# Compras entre R$ 100,00 e R$ 499,99 - 10% de desconto
# Compras iguais ou superiores a R$ 500,00 - 15% de desconto

valor_compra = float(input('Entre com valor da compra: '))
desconto = 0.0

if valor_compra >= 10.00 and valor_compra < 100.00 :
    desconto = 0.05
elif valor_compra < 500:
    desconto = 0.10
elif valor_compra >= 500:
    desconto = 0.15

print(f'Desconto: {desconto * 100}%')
print(f'Valor Final: {valor_compra - (valor_compra * desconto)}')


