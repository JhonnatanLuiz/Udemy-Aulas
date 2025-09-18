"""
aula 55 - imprecisão dos numeros de ponto flutuante + round e decimal
# # round() arredonda um número para o inteiro mais próximo
# # round(2.5) = 2
# decimal.Decimal() é uma classe do módulo decimal que fornece suporte para aritmética decimal com precisão arbitrária.
# # Isso é útil para evitar problemas de precisão com números de ponto flutuante.
Imprecisão dos números de ponto flutuante é um problema comum em programação, especialmente em Python.
# Isso ocorre porque os números de ponto flutuante são representados em binário, o que pode levar a erros de arredondamento.
#Double precision floating point
# # O número 0.1 não pode ser representado exatamente em binário, resultando em uma pequena imprecisão. 
"""
import decimal


numero_1 = decimal.Decimal ('0.1')
numero_2 = decimal.Decimal ('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}') # arredondando para 2 casas decimais
print(round(numero_3, 3)) # arredondando para 3 casas decimais