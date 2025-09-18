"""
aula 53 - enumerate - enumera iteráveis
# enumerate() é uma função embutida que adiciona um contador a um iterável e retorna um objeto enumerado.
"""
lista = ['Jhonnatan', 'Luiz', 'Maria', 'João', 'Ana']
lista.append('Carlos')

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice]) # imprime o índice, o nome e o valor correspondente
# for i in range(len(lista)): # percorre os índices da lista
#     print(i, lista[i]) # imprime o índice e o valor correspondente