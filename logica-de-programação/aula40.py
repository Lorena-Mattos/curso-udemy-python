""" 

Calculadora com while

.lower() -> retorna a mesma string enviada em sair em letras minusculas
.startswith() -> se a string começar com o valor escolhido, ele fará algo
.endwith() -> se a string termina com o valor escolhido, ele fará algo
"""

while True:
    print('nummmmm')
    #########
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break