'''
aula 65 - introdução às funções
Funções são blocos de código reutilizáveis que realizam uma tarefa específica.
Elas podem receber parâmetros de entrada e retornar valores de saída.
As funções ajudam a organizar o código, tornando-o mais legível e modular.
'''

def saudacao(nome):
    """Exibe uma saudação personalizada."""
    print(f'Olá, {nome}! Bem-vindo!')

saudacao('Maria')  # Chama a função saudacao com o parâmetro 'Maria'

# Exemplo 1: Função que retorna a soma de dois números

def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b

resultado = soma(5, 3)
print(f'A soma de 5 e 3 é {resultado}')

# Exemplo 2: Função que verifica se um número é par

def eh_par(numero):
    """Retorna True se o número for par, senão False."""
    return numero % 2 == 0

print(f'4 é par? {eh_par(4)}')
print(f'7 é par? {eh_par(7)}')

# Exemplo 3: Função que imprime uma lista de itens

def imprimir_lista(itens):
    """Imprime cada item de uma lista."""
    for item in itens:
        print(f'- {item}')

imprimir_lista(['maçã', 'banana', 'laranja'])

# Exemplo 4: Função com valor padrão para parâmetro

def saudacao_personalizada(nome, saudacao='Olá'):
    """Exibe uma saudação personalizada com valor padrão."""
    print(f'{saudacao}, {nome}!')

saudacao_personalizada('João')
saudacao_personalizada('Ana', 'Bem-vinda')
