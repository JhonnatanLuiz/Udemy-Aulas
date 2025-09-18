'''
Retorno de valores das funções em Python
# Retorno de valores significa que a função pode retornar um valor
'''

def soma(x, y):
    # Esta função retorna uma lista se x > 10, caso contrário retorna a soma de x e y
    if x > 10:
        return [10, 20]
    return x + y

# Exemplos de uso da função soma
soma1 = soma(2, 2)  # Retorna 4
soma2 = soma(3, 3)  # Retorna 6
print(soma1)
print(soma2)
print(soma(11, 55))  # Retorna [10, 20] porque 11 > 10

# Outro exemplo: função que retorna o maior valor de uma lista

def maior_valor(lista):
    """Retorna o maior valor de uma lista."""
    if not lista:
        return None  # Retorna None se a lista estiver vazia
    else:
        return max(lista)

valores = [5, 8, 2, 10, 3]
print(f'O maior valor da lista é {maior_valor(valores)}')
print(f'O maior valor de uma lista vazia é {maior_valor([])}')