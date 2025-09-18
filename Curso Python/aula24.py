# Operadores in e not in:
# # O operador in verifica se um valor está presente em uma sequência (como uma lista, tupla ou string).
# # O operador not in verifica se um valor não está presente em uma sequência.
# # Ambos retornam um valor booleano (True ou False).
# Strings são iteráveis, ou seja, podem ser percorridas caractere por caractere.
# # Listas também são iteráveis, permitindo verificar a presença de um elemento na lista.
# # Tuplas também são iteráveis, permitindo verificar a presença de um elemento na tupla.
# # Dicionários não são iteráveis, mas você pode verificar a presença de uma chave no dicionário.
# # Conjuntos (sets) são iteráveis, permitindo verificar a presença de um elemento no conjunto.

nome = 'Jhonnatan'
"""print(nome[1])
print(nome[-4]) """
"""print('vio' in nome)
print('zero' in nome)
print(10 * '-')
print('vio' not in nome)
print('zero' not in nome)"""

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} encontrado em {nome}')
else:
    print(f'{encontrar} não encontrado em {nome}')

