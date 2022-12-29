# Formatação com f' strings

nome = 'Lorena'
altura = 1.65
peso = 52
imc = peso / altura ** 2

# formatação de string

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)