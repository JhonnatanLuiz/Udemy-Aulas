# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas a partir de iteráveis.
# Permite criar, filtrar e transformar listas de maneira concisa e eficiente.
import pprint


# Função auxiliar para exibir listas formatadas
def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


# Exemplo tradicional de criação de lista
lista = []
for numero in range(10):
    lista.append(numero)
print('Lista tradicional:', lista)

# Exemplo de list comprehension para criar lista de números dobrados
lista_dobrada = [numero * 2 for numero in range(10)]
print('Lista dobrada:', lista_dobrada)

# Exemplo de list comprehension com filtro (apenas números menores que 5)
lista_filtrada = [n for n in range(10) if n < 5]
print('Lista filtrada (<5):', lista_filtrada)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30},
]

# Aumenta o preço em 5% apenas dos produtos com preço maior que 20
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]
print('Produtos com aumento de preço:', novos_produtos)

# List comprehension com filtro e transformação
novos_produtos_filtrados = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
]
print('Produtos filtrados e transformados:')
p(novos_produtos_filtrados)

# Mais exemplos:
# List comprehension para criar lista de quadrados
quadrados = [x ** 2 for x in range(10)]
print('Quadrados:', quadrados)

# List comprehension para inverter strings
nomes = ['Ana', 'João', 'Maria']
nomes_invertidos = [nome[::-1] for nome in nomes]
print('Nomes invertidos:', nomes_invertidos)

# Explicação:
# - List comprehension permite criar listas de forma compacta e legível.
# - Pode incluir filtros (if) e transformações.
# - É útil para mapeamento, filtragem e manipulação de dados em listas.