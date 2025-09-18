# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer outra em Python.
# Porém, são funções anônimas que contêm apenas uma linha (uma expressão).
# São úteis para operações rápidas, especialmente como argumento de funções como sorted, map, filter, etc.

# Lista de dicionários com nomes e sobrenomes
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]


# Função para exibir a lista formatada
def exibir(lista):
    for item in lista:
        print(item)
    print()


# Ordena a lista pelo nome usando lambda como chave de ordenação
l1 = sorted(lista, key=lambda item: item['nome'])
# Ordena a lista pelo sobrenome usando lambda como chave de ordenação
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)

# Outros exemplos de função lambda:

# Exemplo 1: função para somar dois números
def soma(x, y):
    return x + y
print('Soma de 2 e 3:', soma(2, 3))

# Exemplo 2: função para elevar ao quadrado
def quadrado(x):
    return x ** 2
print('Quadrado de 5:', quadrado(5))

# Exemplo 3: lambda com map para dobrar valores de uma lista
numeros = [1, 2, 3, 4]
dobrados = list(map(lambda x: x * 2, numeros))
print('Números dobrados:', dobrados)

# Exemplo 4: lambda com filter para filtrar números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print('Números pares:', pares)

# Explicação:
# - O código principal mostra como usar lambda para ordenar listas de dicionários.
# - Os exemplos extras mostram lambda em operações matemáticas, map e filter.
# - Lambdas são úteis para funções simples e rápidas, sem a necessidade de definir uma função completa com def.