"""
Iterando strings com while
"""
#       012345678910
# nome = 'Luiz Otávio'  # Iteráveis
#       1110987654321
# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[3])

# nova_string = ''
# nova_string += '*L*u*i*z* *O*t*á*v*i*o'


# resolução de exercício de iteração de str com while
nome = 'Luiz Otávio'  # Iteráveis

tamanho_nome = len(nome)

indice = 0

novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)