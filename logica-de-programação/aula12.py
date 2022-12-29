# Exercício para calcular IMC

nome = input('Qual é seu nome? ').capitalize()

idade = input('Qual é sua idade? ')

altura = float(input('Qual é a sua altura? '))

peso = int(input('Quanto você pesa? '))

imc = peso / altura ** 2

result = f'{nome} tem {altura:.2f} de altura, sua idade é {idade} anos e pesa {peso} Kg. Seu IMC é: {imc}'
print(nome, result)

if imc <= 18.5:
    print(nome, 'cuidado, seu IMC indica magreza')
    
elif imc >= 18.5:
    print(nome, 'seu IMC está normal')
elif imc >= 24.9:
    print(nome, 'seu IMC indica sobrepeso')
elif imc >= 30:
    print(nome, 'cuidado, seu IMC indica obesidade')
else:
    print('Não há indicações de IMC')

