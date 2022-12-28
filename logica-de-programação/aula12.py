# Exercício para calcular IMC

nome = input('Qual é seu nome? ').capitalize()
print('Nome:', nome)

idade = input('Qual é sua idade? ')
print('Idade: ', idade, 'anos')

altura = float(input('Qual é a sua altura? '))
print('Altura: ', altura)

peso = int(input('Quanto você pesa? '))
print('Peso: ', peso, 'Kg')

imc = peso / altura ** 2
print('Seu IMC é: ', imc)

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
