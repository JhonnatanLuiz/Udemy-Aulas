#nome = input('Qual é o seu nome?')
#print(f'O seu nome é {nome=}')

numero_1 = input('Digite um número: ') # input sempre retorna uma string
# input() é uma função que lê a entrada do usuário e retorna como string.
# O valor retornado é sempre uma string, mesmo que o usuário digite um número.
numero_2 = input('Digite outro número: ') # input() é uma função que lê a entrada do usuário e retorna como string.
# O valor retornado é sempre uma string, mesmo que o usuário digite um número.

int_numero_1 = int(numero_1) # int() converte uma string em um número inteiro.
# int() é uma função que converte um valor em um número inteiro.
int_numero_2 = int(numero_2)

print(f'A soma dos números é {int(numero_1) + int(numero_2)}') # A soma dos números é 11