# Este código demonstra o uso de desempacotamento de listas, tuplas e strings em chamadas de funções e métodos em Python.
# O desempacotamento permite passar os elementos de uma coleção como argumentos separados para funções, métodos ou prints.

# Definição de uma string
string = 'ABCD'

# Definição de uma lista com diferentes tipos de elementos
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']

# Definição de uma tupla
tupla = 'Python', 'é', 'legal'

# Lista de listas (salas), cada sublista representa uma sala com nomes de pessoas
salas = [
    ['Maria', 'Helena', ],  # Sala 0
    ['Elaine', ],           # Sala 1
    ['Luiz', 'João', 'Eduarda', ],  # Sala 2
]

# Exemplos de desempacotamento (comentados):
# p, b, *_, ap, u = lista  # Desempacota elementos da lista em variáveis
# print(p, u, ap)          # Imprime variáveis desempacotadas

# print('Maria', 'Helena', 1, 2, 3, 'Eduarda')  # Imprime elementos separadamente
# print(*lista)            # Desempacota e imprime todos os elementos da lista
# print(*string)           # Desempacota e imprime cada caractere da string
# print(*tupla)            # Desempacota e imprime cada elemento da tupla

# Desempacota cada sublista de 'salas' e imprime uma por linha
print(*salas, sep='\n')