'''
aula 66 - Argumentos nomeados e argumentos posicionais (não nomeados) em funções
# Argumentos nomeados permitem passar argumentos para funções usando o nome do parâmetro, enquanto argumentos posicionais são passados na ordem em que os parâmetros são definidos.
'''

def soma(x, y, z):
    # Definição da função soma com três parâmetros
    # x, y, z podem ser passados por posição ou nome
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)

# Exemplo de chamada com argumentos posicionais (ordem importa)
soma(1, 2, 3)
# Exemplo de chamada com argumento nomeado (y=2, z=5)
soma(1, y=2, z=5)

# Exemplo de uso de argumentos nomeados na função print
print(1, 2, 3, sep='-')

# Outro exemplo prático:
def apresentar_pessoa(nome, idade, cidade):
    print(f'Nome: {nome} | Idade: {idade} | Cidade: {cidade}')

# Chamada com argumentos posicionais
apresentar_pessoa('Ana', 30, 'São Paulo')
# Chamada com argumentos nomeados (ordem não importa)
apresentar_pessoa(idade=25, cidade='Rio de Janeiro', nome='Carlos')