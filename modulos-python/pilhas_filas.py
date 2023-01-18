# Pilhas e filas
# Pilha é uma estrutura de dados que segue o princípio LIFO
# (Last In, First Out)
# ou seja, o último elemento a entrar é o primeiro a sair
# Exemplo: Uma fila de banco (ou qualquer fila da vida real)
# Filas podem ter efeitos colaterais em desempenho, porque a cada item
# alterado, todos os indices serão modificados.

from collections import deque
from time import sleep

fila = deque(maxlen=10)
fila.extend([10, 20, 30, 40, 50, 60, 70, 80])
fila.rotate(2)
print(fila)
