from sys import path

import aula99_package.modulo
from aula99_package import modulo
from aula99_package.modulo import *

# from aula99_package.modulo import soma_do_modulo

# print(*path, sep='\n')
print(soma_do_modulo(1, 2))
print(aula99_package.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
print(variavel)
print(nova_variavel)

# __all__ = [
#     'variavel',
#     'soma_do_modulo',
#     'nova_variavel',
# ]

variavel = 'Alguma coisa'


def soma_do_modulo(x, y):
    return x + y


nova_variavel = 'OK'