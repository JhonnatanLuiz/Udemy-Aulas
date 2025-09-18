# Empacotamento e desempacotamento de dicionários + *args e **kwargs
# Exemplo de troca de valores entre variáveis
a, b = 1, 2
a, b = b, a  # Troca os valores de a e b
# print(a, b)

# Exemplo de desempacotamento de dicionário com .items()
# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

# Dicionários de exemplo
pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

# Unindo dois dicionários usando o operador ** (desempacotamento)
pessoas_completa = {**pessoa, **dados_pessoa}
# print(pessoas_completa)

# args e kwargs
# args: argumentos posicionais (não nomeados)
# kwargs: keyword arguments (argumentos nomeados)


def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)  # Mostra os argumentos posicionais
    for chave, valor in kwargs.items():  # Percorre os argumentos nomeados
        print(chave, valor)


# Exemplos de uso:
# mostro_argumentos_nomeados(nome='Joana', qlq=123)
# mostro_argumentos_nomeados(**pessoas_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)  # Passa os itens do dicionário como argumentos nomeados

# Outro exemplo: combinando argumentos posicionais e nomeados


def exemplo_args_kwargs(*args, **kwargs):
    print('Posicionais:', args)
    print('Nomeados:', kwargs)


exemplo_args_kwargs(10, 20, 30, nome='Maria', idade=25)

# Explicação:
# - O código mostra como empacotar e desempacotar dicionários usando **.
# - Mostra como usar *args para argumentos posicionais e **kwargs para argumentos nomeados em funções.
# - Os exemplos ilustram como passar e acessar esses argumentos em funções Python.