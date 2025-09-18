'''
Closure e funções que retornam outras funções
# Closure é uma função que lembra o ambiente onde foi criada, mesmo após o escopo original ter sido encerrado.
'''

def criar_saudacao(saudacao):
    # Função externa recebe uma saudação
    def saudar(nome):
        # Função interna lembra da saudação recebida
        return f'{saudacao}, {nome}!'
    return saudar  # Retorna a função interna

# Exemplo de uso do closure:
falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))

# Outro exemplo: closure para multiplicação

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

multiplica_por_2 = criar_multiplicador(2)
multiplica_por_5 = criar_multiplicador(5)

print(multiplica_por_2(10))  # 20
print(multiplica_por_5(3))   # 15

# Outro exemplo: contador com closure

def contador():
    total = 0
    def incrementar():
        nonlocal total
        total += 1
        return total
    return incrementar

meu_contador = contador()
print(meu_contador())  # 1
print(meu_contador())  # 2
print(meu_contador())  # 3

# Explicação:
# - Closure permite que funções internas "lembrem" do ambiente onde foram criadas.
# - Isso é útil para criar funções personalizadas e manter estados entre chamadas.