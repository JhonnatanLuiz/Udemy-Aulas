# isinstace - para saber se objeto é de determinado tipo
lista = [
    'a',  # string
    1,    # inteiro
    1.1,  # float
    True, # booleano
    [0, 1, 2],  # lista
    (1, 2),     # tupla
    {0, 1},     # set
    {'nome': 'Luiz'},  # dicionário
]

for item in lista:
    # Verifica se o item é um set
    if isinstance(item, set):
        print('SET')
        item.add(5)  # Adiciona o valor 5 ao set
        print(item, isinstance(item, set))  # Mostra o set e confirma o tipo

    # Verifica se o item é uma string
    elif isinstance(item, str):
        print('STR')
        print(item.upper())  # Mostra a string em maiúsculo

    # Verifica se o item é um número inteiro ou float
    elif isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)  # Mostra o número e seu dobro

    # Caso não seja nenhum dos tipos acima
    else:
        print('OUTRO')
        print(item)  # Mostra o item original

# Explicação:
# - O código percorre uma lista com diferentes tipos de dados.
# - Usa isinstance para identificar o tipo de cada item.
# - Executa uma ação diferente para cada tipo: set, string, número, ou outros.
# - Demonstra como tratar tipos diferentes de dados em uma mesma estrutura.