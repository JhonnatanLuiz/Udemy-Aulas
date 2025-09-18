# precendencia de operadores
# A precedência de operadores define a ordem em que as operações são realizadas em uma expressão.
# Os operadores com maior precedência são avaliados primeiro.
# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
conta_1 = 1 + 1 ** 5 + 5
print(conta_1)  # Resultado: 7 (1 + 1 + 5 = 7)

conta_2 = (1 + 1) ** (5 + 5)
print(conta_2)  # Resultado: 1024 ((1 + 1) ** (5 + 5) = 1024)