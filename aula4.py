# Tipos int e float
# int -> Número inteiro
# O tipo int representa qualquer número
# positivo ou negativo. int sem sinal é considerado positivo

print(11) # int
print(-11) # int
print(0)

# float -> Número com pontos flutuantes
# O tipo float representa qualquer número
# positivo ou negativo com pontos flutuante.
# float sem sinal é considerado positivo.

print(1.1) # float
print(0.0, -1.5) # float

# A função type mostra o tipo que o Python inferiu ao valor.

print(type(12.3)) # float
print(type(12)) # int
print(type('Lorena')) # str

print(type('Lorena'), type(1.2), type(2))