"""
Interpolação básica de strings

s - string
d e i - int
f - float
x e x - Hexadecimal (ABCDEF0123456789)
"""

# Exemplos:

nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço total é R$%.2f' % (nome, preco)
print(variavel)

print(33 * '-')
print('O hexadecimal de %d é %08X' % (1500, 1500)) # Pode ser usado 4 ou 8, com x maiúsculo para colocar letras maiúsculas ou x minusculo
