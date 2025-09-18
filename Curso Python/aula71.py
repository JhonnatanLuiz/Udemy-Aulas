'''
argumentos para quantidade de argumentos não nomeados variáveis
*args
# Exemplo de uso do *args para receber múltiplos argumentos
'''

# Exemplo de desempacotamento de variáveis
x, y, *resto = 1, 2, 3, 4, 5, 6
print(x, y, resto)  # x=1, y=2, resto=[3, 4, 5, 6]

# Exemplo 1: Função que soma todos os argumentos recebidos

def soma(*args):
    """Soma todos os argumentos passados."""
    total = 0
    for num in args:
        print('Total', total, num)
        total = total + num
    print(total)

soma(1, 2, 3, 4, 5)

# Exemplo 2: Função que multiplica todos os argumentos recebidos

def multiplica(*args):
    """Multiplica todos os argumentos passados."""
    resultado = 1
    for num in args:
        resultado *= num
    print(f'Resultado da multiplicação: {resultado}')

multiplica(2, 3, 4)

# Exemplo 3: Função que imprime todos os argumentos recebidos

def imprime_args(*args):
    """Imprime todos os argumentos recebidos."""
    for i, valor in enumerate(args):
        print(f'Argumento {i}: {valor}')

imprime_args('a', 'b', 'c', 1, 2, 3)

# Exemplo 4: Função que usa sum para somar todos os argumentos

def soma_com_sum(*args):
    """Soma todos os argumentos usando a função sum do Python."""
    resultado = sum(args)
    print(f'Soma com sum: {resultado}')

soma_com_sum(10, 20, 30, 40)

