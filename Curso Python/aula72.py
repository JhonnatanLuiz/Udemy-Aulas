# Exercícios com funções

# Função que multiplica todos os argumentos não nomeados recebidos
# Retorna o total para uma variável e mostra o valor da variável

def multiplica(*args):
    """Multiplica todos os argumentos recebidos e retorna o resultado."""
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

# Exemplo de uso da função multiplica
produto = multiplica(2, 3, 4)
print(f'O resultado da multiplicação é: {produto}')

# Função que fala se um número é par ou ímpar
# Retorna se o número é par ou ímpar

def par_ou_impar(numero):
    """Retorna se o número é par ou ímpar."""
    if numero % 2 == 0:
        return 'par'
    else:
        return 'ímpar'

# Exemplo de uso da função par_ou_impar
resultado_par_impar = par_ou_impar(7)
print(f'O número 7 é {resultado_par_impar}')
resultado_par_impar = par_ou_impar(10)
print(f'O número 10 é {resultado_par_impar}')

# Explicação:
# A função multiplica usa *args para receber vários argumentos e multiplica todos eles, retornando o resultado.
# A função par_ou_impar recebe um número e retorna 'par' se for divisível por 2, senão retorna 'ímpar'.
# Os exemplos mostram como usar cada função e exibem os resultados no console.