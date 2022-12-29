# Operadores lógicos
# And (e) Or (ou) Not (não)
# and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# São consideradas falsy (que você já viu) 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor

# Exemplo

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

# if True:
# ...

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')

else:
    print('Sair')

# Avaliação de curto circuito
# print(True and False and True)
# print(True and 0 and True) # -> para na condição zero ou false