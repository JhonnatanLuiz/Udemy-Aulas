"""
aula 44 - Introdução ao For+Range = estrutura de repetição para coisas finitas
# Este código percorre uma string e conta quantas vezes cada letra aparece, ignorando espaços.
# for = estrutura de repetição para coisas finitas
Range = função que gera uma sequência de números inteiros em um intervalo especificado.
(start, stop, step) = parâmetros que definem o intervalo e o passo da sequência.
"""
numeros = range(0, 100, 10)  # Gera números de 0 a 90 com passo de 10
# range(0, 100, 10) = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

for numero in numeros:
    print(numero)