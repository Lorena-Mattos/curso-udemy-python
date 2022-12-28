# Exercício para calcular IMC

nome = input('Qual é seu nome? ')
print('Nome:', nome)

idade = input('Qual é sua idade? ')
print('Idade: ', idade)

altura = float(input('Qual é a sua altura? '))
print('Altura: ', altura)

peso = int(input('Quanto você pesa? '))
print('Peso: ', peso)

imc = peso / (altura * altura)
print(imc)

if imc <= 18.5:
    print('Cuidado, seu imc indica magreza')
    
elif imc >= 18.5:
    print('Seu IMC está normal')
elif imc >= 24.9:
    print('Você está com sobrepeso')
elif imc >= 30:
    print('Cuidado, seu IMC indica obesidade')
else:
    print('Não há indicações de IMC')
