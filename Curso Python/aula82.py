# Função executa recebe uma função e argumentos, e executa a função com esses argumentos
# Isso permite passar funções e argumentos dinamicamente

def executa(funcao, *args):
    return funcao(*args)

# Exemplo comentado de função soma
# def soma(x, y):
#     return x + y

# Exemplo comentado de closure para criar multiplicadores
# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica

# Exemplo de closure usando lambda:
# duplica recebe uma função que multiplica por 2
# lambda m: lambda n: n * m cria uma função que retorna outra função
# executa(lambda m: lambda n: n * m, 2) retorna lambda n: n * 2
# duplica(2) retorna 4

duplica = executa(
    lambda m: lambda n: n * m,
    2
)
print(duplica(2))  # Saída: 4

# Exemplo de soma usando executa e lambda
print(
    executa(
        lambda x, y: x + y,
        2, 3
    ),  # Saída: 5
)

# Exemplo de soma de vários argumentos usando *args e sum
print(
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )  # Saída: 28
)

# Explicação:
# - O código mostra como passar funções anônimas (lambda) e argumentos para uma função executora.
# - Mostra closure com lambda, soma simples e soma de vários argumentos.
# - Isso ilustra o conceito de funções de primeira classe e funções de ordem superior em Python.