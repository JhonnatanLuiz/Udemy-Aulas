'''
Exercicio
Crie funções que dupliquem, tripliquem e quadruplicam
o número recebido como parâmetro.
Solução usando closure para evitar repetição de código.
'''

def criar_multiplicador(multiplicador):
    """Retorna uma função que multiplica o número pelo multiplicador informado."""
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

# Cria funções específicas usando o closure
duplica = criar_multiplicador(2)
triplica = criar_multiplicador(3)
quadruplica = criar_multiplicador(4)

# Exemplos de uso das funções
numero = 5
print(f'Dobro de {numero}: {duplica(numero)}')
print(f'Triple de {numero}: {triplica(numero)}')
print(f'Quádruplo de {numero}: {quadruplica(numero)}')

# Explicação:
# - A função criar_multiplicador retorna uma função personalizada para multiplicar pelo valor desejado.
# - Isso evita repetição de código e facilita criar outros multiplicadores se necessário.