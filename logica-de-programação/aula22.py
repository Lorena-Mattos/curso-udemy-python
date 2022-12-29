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

# quando a operação está dentro de (), ela será avaliada primeiro, no caso em tela usamos a operação Or e And
# Para que o código não fique dificil de compreender, o () é uma alternativa para que esse trecho seja avaliado primeiro

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')

else:
    print('Sair')

# Avaliação de curto circuito:

# senha = 0 or False or 0 or 'abc' or True
# print(senha)

# senha = input('Senha: ') or 'Sem senha'
# print(senha)

# print(True or False)
# print(True or 0 or False or 'abc') # -> irá retornar o último valor que for considerado verdadeiro