# Dictionary Comprehension e Set Comprehension
# Exemplo de dictionary comprehension para transformar valores em maiúsculo (se forem string)
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

# Cria um novo dicionário com valores em maiúsculo para strings, exceto a chave 'categoria'
dc = {
    chave: valor.upper()  # Transforma em maiúsculo se for string
    if isinstance(valor, str) else valor  # Mantém valor se não for string
    for chave, valor
    in produto.items()
    if chave != 'categoria'  # Exclui a chave 'categoria'
}
# print(dc)

# Exemplo de dictionary comprehension a partir de uma lista de tuplas
lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),  # Chaves duplicadas: o último valor prevalece
]
dc = {
    chave: valor
    for chave, valor in lista
}
# print(dc)

# Exemplo de set comprehension para criar um conjunto de potências de 2
s1 = {2 ** i for i in range(10)}  # Cria um set com 2 elevado a cada valor de 0 a 9
print(s1)

# Explicação:
# - Dictionary comprehension permite criar dicionários de forma concisa, aplicando transformações e filtros.
# - No exemplo, valores string são convertidos para maiúsculo, exceto para a chave 'categoria'.
# - Ao criar dicionário de uma lista de tuplas, chaves duplicadas são sobrescritas pelo último valor.
# - Set comprehension permite criar conjuntos de forma rápida, como o conjunto das potências de 2.