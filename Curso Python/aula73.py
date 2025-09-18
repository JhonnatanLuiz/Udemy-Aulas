'''
Academicamente, os termos Higher Order Functions e First-Class Functions têm significados diferentes.

Higher Order Functions - Funções que podem receber e/ou retornar outras funções
First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)
'''

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

# Exemplo de Higher Order Function: executa recebe uma função e argumentos

def executa(funcao, *args):
    return funcao(*args)

print(
    executa(saudacao, 'Bom dia', 'Luiz')
)
print(
    executa(saudacao, 'Boa noite', 'Maria')
)

# Outro exemplo: função que recebe outra função como argumento

def ao_quadrado(x):
    return x * x

def aplica_funcao(funcao, lista):
    """Aplica uma função a todos os elementos de uma lista."""
    return [funcao(item) for item in lista]

numeros = [1, 2, 3, 4]
quadrados = aplica_funcao(ao_quadrado, numeros)
print('Quadrados:', quadrados)

# Outro exemplo: função que retorna outra função (closure)

def criar_multiplicador(fator):
    def multiplicar(numero):
        return numero * fator
    return multiplicar

multiplica_por_3 = criar_multiplicador(3)
print('Multiplica por 3:', multiplica_por_3(10))
print('Multiplica por 3:', multiplica_por_3(7))

# Explicação:
# - First-Class Functions: funções podem ser passadas como argumentos, retornadas e atribuídas a variáveis.
# - Higher Order Functions: funções que recebem ou retornam outras funções, como executa, aplica_funcao e criar_multiplicador.