# Precedência dos operadores
# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + - 

conta_1 = 1 + 1 ** 5 + 5 # 7 sem paretese, com o resultado é 1024
print(conta_1)

conta_1 = (1 + 1) ** (5 + 5) # 1024 com paretese, sem o resultado é 7
print(conta_1)

conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5) # 1024 com paretese e int
print(conta_1)
