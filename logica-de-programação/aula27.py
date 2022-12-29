"""
Fatiamento de strings
012345678
Olá mundo
-987654321

Fatiamento [i:f:p] [::]
Obs.: a função len retorna a quantidade de caracteres da str
"""

variavel = 'Olá mundo'
print(variavel[5]) # indice especifico é: u
print(variavel[-4]) # indice especifico é: u, aqui usamos números negativos

print(33 * '-')
print(variavel[:5]) # fatiamento, lembrando que ele sempre exclui o último indice, nesse caso o fatiamento vai do Olá ao m
print(variavel[0:5]) # fatiamento, lembrando que ele sempre exclui o último indice, nesse caso o fatiamento vai do Olá ao m
print(variavel[-8:-2])# fatiamento, lembrando que ele sempre exclui o último indice, nesse caso o fatiamento vai do lá ao mun

# o espaço é um caractere 

print(len(variavel)) # contagem de caractere
print(variavel[0:len(variavel):1]) # contando do 0 de um em um
print(variavel[0:9:2]) # conta do 0 a 9, de 2 em 2
print(variavel[::-1]) # conta do 0 a 9, só que de forma invertida, contando de trás pra frente