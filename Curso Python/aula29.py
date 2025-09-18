"""
Aula 29 - Introdução ao try/except
try/except é uma estrutura de controle de fluxo que permite lidar com exceções (erros) em Python.
Quando um erro ocorre dentro do bloco try, o fluxo de execução é interrompido e o controle é transferido para o bloco except correspondente.
O bloco except é executado quando uma exceção específica ocorre, permitindo que você trate o erro de maneira adequada.
O bloco try/except é útil para evitar que o programa seja interrompido abruptamente devido a erros inesperados, 
permitindo que você forneça mensagens de erro amigáveis ou execute ações alternativas.

"""
numero_str = input('Vou dobrar o número que você digitar: ')

try:
    numero_float = float(numero_str)
    print('float:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except ValueError:
    print('Você não digitou um número válido.') 

    """print(numero_str.isdigit())

numero_float = float(numero_str)
print(f'O dobro de {numero} é {int(numero) * 2:.2f}')"""