import copy

# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo par de "chave" e "valor".
# Chaves funcionam como índices, mas podem ser de tipos imutáveis (str, int, float, bool, tuple).
# Os valores podem ser de qualquer tipo, inclusive listas ou outros dicionários.
# Usamos as chaves - {} - ou a classe dict para criar dicionários.
# Exemplo de dicionário:
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# Também é possível criar usando dict():
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

pessoa = {
    'nome': 'Luiz Otávio',  # chave 'nome' com valor string
    'sobrenome': 'Miranda', # chave 'sobrenome' com valor string
    'idade': 18,            # chave 'idade' com valor inteiro
    'altura': 1.8,          # chave 'altura' com valor float
    'endereços': [          # chave 'endereços' com valor lista de dicionários
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}

# Acessando valores pelas chaves
print(pessoa['nome'])      # Imprime o valor associado à chave 'nome'
print(pessoa['sobrenome']) # Imprime o valor associado à chave 'sobrenome'

print()

# Percorrendo as chaves do dicionário
for chave in pessoa:
    # Aqui, 'chave' será cada chave do dicionário pessoa
    # Exemplo: 'nome', 'sobrenome', 'idade', 'altura', 'endereços'
    pass  # Substitua por print(chave) ou outra operação se desejar

# Exemplo de Shallow Copy (cópia rasa) e Deep Copy (cópia profunda) com objetos mutáveis em Python

# Lista com listas internas (mutável)
lista_original = [[1, 2], [3, 4]]

# Shallow Copy: copia apenas o objeto externo, referências internas são compartilhadas
lista_shallow = copy.copy(lista_original)

# Deep Copy: copia o objeto externo e todos os objetos internos (recursivamente)
lista_deep = copy.deepcopy(lista_original)

# Modificando um elemento interno da lista original
lista_original[0][0] = 99

print('Original:', lista_original)      # [[99, 2], [3, 4]]
print('Shallow Copy:', lista_shallow)   # [[99, 2], [3, 4]] (referência compartilhada)
print('Deep Copy:', lista_deep)         # [[1, 2], [3, 4]]   (independente)

# Explicação:
# - Shallow Copy: alterações em objetos internos afetam todas as cópias, pois compartilham referência.
# - Deep Copy: alterações em objetos internos NÃO afetam a cópia profunda, pois tudo é copiado recursivamente.
# - Use copy.copy() para shallow copy e copy.deepcopy() para deep copy.

# Exemplos de métodos pop, popitem e update em dicionários

# Dicionário de exemplo
meu_dict = {'a': 1, 'b': 2, 'c': 3}

# pop: remove e retorna o valor da chave especificada
valor_removido = meu_dict.pop('b')
print('Após pop:', meu_dict)         # {'a': 1, 'c': 3}
print('Valor removido:', valor_removido)  # 2

# popitem: remove e retorna o último par chave-valor inserido
chave, valor = meu_dict.popitem()
print('Após popitem:', meu_dict)     # {'a': 1}
print('Chave e valor removidos:', chave, valor)

# update: atualiza o dicionário com outro dicionário ou pares chave-valor
meu_dict.update({'d': 4, 'e': 5})
print('Após update:', meu_dict)      # {'a': 1, 'd': 4, 'e': 5}

# Explicação:
# - pop('chave') remove a chave especificada e retorna seu valor.
# - popitem() remove o último item inserido e retorna (chave, valor).
# - update({...}) adiciona ou atualiza pares chave-valor no dicionário.