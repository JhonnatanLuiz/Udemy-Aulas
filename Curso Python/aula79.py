'''
Exemplo de uso dos sets em Python
# Demonstrando o uso de sets com operações comuns
'''

# Cria um set vazio para armazenar letras digitadas
letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())  # Adiciona a letra (em minúsculo) ao set

    if 'l' in letras:  # Verifica se a letra 'l' já foi digitada
        print('PARABÉNS')
        break

    print(letras)  # Mostra o set de letras já digitadas

# Outros exemplos de sets em Python:

# Exemplo 1: Remover duplicados de uma lista
numeros = [1, 2, 2, 3, 4, 4, 5]
sem_duplicados = set(numeros)
print('Sem duplicados:', sem_duplicados)

# Exemplo 2: Operações de conjuntos
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print('União:', set_a | set_b)           # {1, 2, 3, 4, 5}
print('Interseção:', set_a & set_b)      # {3}
print('Diferença:', set_a - set_b)       # {1, 2}
print('Diferença simétrica:', set_a ^ set_b)  # {1, 2, 4, 5}

# Exemplo 3: Métodos add, update, discard, clear
s = set()
s.add(10)
s.update([20, 30])
print('Set após add e update:', s)
s.discard(20)
print('Set após discard:', s)
s.clear()
print('Set após clear:', s)

# Explicação:
# - O set armazena apenas valores únicos.
# - Métodos e operações permitem manipular conjuntos de forma eficiente.
# - Sets são úteis para testes de existência, remoção de duplicados e operações matemáticas de conjuntos.