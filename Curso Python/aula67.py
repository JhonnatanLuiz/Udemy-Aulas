'''
aula 67 - Valores padrão para parâmetros em funções
# Valores padrão permitem definir um valor para um parâmetro caso nenhum valor seja passado na chamada da função.
# Refatorar = editar o código para melhorar sua legibilidade ou funcionalidade sem alterar seu comportamento externo.
'''

def soma(x, y, z=None):
    # Função soma com valor padrão para z (None)
    # Se z não for passado, soma apenas x e y
    # Se z for passado, soma x, y e z
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)


soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)
soma(y=9, z=0, x=7)

# Outro exemplo: função de saudação com valor padrão

def saudacao(nome, mensagem='Olá'):
    """Exibe uma saudação personalizada, com valor padrão para mensagem."""
    print(f'{mensagem}, {nome}!')

saudacao('Maria')  # Usa valor padrão 'Olá'
saudacao('João', 'Bem-vindo')  # Usa mensagem personalizada