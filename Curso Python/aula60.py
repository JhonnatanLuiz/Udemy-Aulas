'''
Operação ternária (condicional de uma linha)
<valor> if <condição> else <outro valor>
A operação ternária permite fazer atribuições ou retornar valores com base em uma condição, tudo em uma única linha.
'''
# Exemplo de condição simples:
# condicao = 10 == 11
# variavel = 'Valor' if condicao else 'Outro valor'  # Se condicao for True, retorna 'Valor', senão 'Outro valor'
# print(variavel)

# Exemplo prático com números:
# digito = 9  # > 9 = 0
# novo_digito = digito if digito <= 9 else 0  # Se digito for menor ou igual a 9, mantém o valor, senão vira 0
# novo_digito = 0 if digito > 9 else digito   # Outra forma de escrever a mesma lógica
# print(novo_digito)

# Exemplo de múltiplas condições aninhadas:
# print('Valor' if False else 'Outro valor' if False else 'Fim')  # Imprime 'Fim' pois todas as condições anteriores são False

# Outro exemplo de operação ternária:
idade = 18
maioridade = 'Maior de idade' if idade >= 18 else 'Menor de idade'
print(maioridade)  # Imprime 'Maior de idade' pois idade é 18