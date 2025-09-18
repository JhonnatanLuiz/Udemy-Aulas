'''
aula 57 - Lista de listas e seus índices
# # # Uma lista de listas é uma lista que contém outras listas como elementos.
# # # Isso é útil para armazenar dados em uma estrutura de tabela, onde cada sublista representa uma linha e cada elemento da sublista representa uma coluna.
# # # Para acessar os elementos de uma lista de listas, você pode usar dois índices: o primeiro índice para a lista externa e o segundo índice para a lista interna.
# # # Por exemplo, se você tiver uma lista de listas chamada "matriz", você pode acessar o elemento na linha i e coluna j usando matriz[i][j].
# # # Você também pode usar loops aninhados para percorrer todos os elementos de uma lista de listas.
# # # Para adicionar ou remover elementos de uma lista de listas, você pode usar os métodos append() e remove() da lista.
'''
salas = [
    ['Jhonnatan', 'Luiz', 'Maria', 'João', 'Ana'],
    ['Carlos', 'Fernanda', 'Pedro', 'Lucas'],
    ['Mariana', 'Roberto', 'Juliana']
]

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(f'O aluno é {aluno}')
print('---' * 20)