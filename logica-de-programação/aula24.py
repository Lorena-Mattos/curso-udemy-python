# Operadores in (está entre) e not in (não está entre)
# Strings são iteráveis
# 0 1 2 3 4 5
# O t á v i o
# -6-5-4-3-2-1

# Como acessar os índices: 

nome = 'Otávio'
print(nome[2]) # colocar número do indice entre []
print(nome[-4]) # número negativo também acessa o indice, sempre entre []

print(10 * '-')
print('á' in nome) # se a letra estiver, ele retorna True
print('z' in nome) # se não estiver, retorna False

# not in vai inverter
print(10 * '-')
print('vio' not in nome) # se a letra estiver, ele retorna False
print('zero' not in nome) # se não estiver, retorna True

# Exemplo:

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')

else:
    print(f'{encontrar} não está em {nome}')