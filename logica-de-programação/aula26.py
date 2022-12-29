"""
Formatação de strings com f-strings

s - string
d - int
f - float

.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)

> - Esquerda
< - Direita
^ - Centro

Sinal: + ou -
Ex.: 0>100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{variavel:$^10}.')
print(f'{1000.4873645565646:,.1f}')
print(f'{1000.4873645565646:.2f}')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')
print(f'{variavel!s}')
print(f'{variavel!a}')