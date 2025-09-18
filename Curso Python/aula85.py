'''
List comprehension com mais de um for
'''
# Exemplo tradicional com dois loops for aninhados
lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))  # Adiciona tuplas (x, y) para cada combinação

# List comprehension equivalente ao exemplo acima
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
# Cria uma lista de tuplas para cada combinação de x e y

# List comprehension com dois for, gerando listas internas
lista = [
    [(x, letra) for letra in 'Luiz']  # Para cada x, cria uma lista de tuplas (x, letra)
    for x in range(3)
]
# Resultado: lista de listas, cada uma contendo tuplas com x e cada letra de 'Luiz'

print(lista)  # Exibe o resultado final

# Explicação:
# - O primeiro exemplo mostra como criar todas as combinações de x e y usando dois for aninhados.
# - O segundo exemplo faz o mesmo usando list comprehension, tornando o código mais compacto.
# - O terceiro exemplo cria uma lista de listas, onde cada sublista contém tuplas de x com cada letra da string 'Luiz'.
# - List comprehensions com múltiplos for são úteis para gerar combinações, produtos cartesianos e estruturas aninhadas.