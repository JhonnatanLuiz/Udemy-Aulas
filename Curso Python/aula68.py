'''
aula 68 - Escopo de funções e variáveis locais e globais
# O escopo de uma variável determina onde ela pode ser acessada no código.
# Variáveis locais são definidas dentro de uma função e só podem ser acessadas dentro dela.
# Variáveis globais são definidas fora de funções e podem ser acessadas em qualquer parte do código, incluindo dentro de funções.
'''

x = 1  # Variável global

def escopo():
    global x  # Indica que vamos usar a variável global x
    x = 10  # Altera o valor da variável global x

    def outra_funcao():
        global x  # Indica que vamos usar a variável global x
        x = 11  # Altera novamente o valor da variável global x
        y = 2  # Variável local à função outra_funcao
        print(x, y)  # Imprime o valor de x (global) e y (local)

    outra_funcao()  # Chama a função interna
    print(x)  # Imprime o valor de x após a execução de outra_funcao

print(x)  # Imprime o valor inicial de x (global)
escopo()  # Chama a função escopo, que altera x
print(x)  # Imprime o valor final de x (global) após as alterações
