# interpolação básica de strings
# # A interpolação de strings é o processo de inserir valores em uma string, substituindo marcadores de posição por valores reais.
# # Em Python, isso pode ser feito usando o método format() ou f-strings (Python 3.6+).
# # O método format() permite inserir valores em uma string usando chaves {} como marcadores de posição.
# # As f-strings (formatted string literals) permitem incluir expressões diretamente dentro de uma string, precedendo a string com a letra 'f'.
# # Ambas as abordagens são úteis para criar strings dinâmicas e formatadas.
# Hexadecimal: O sistema hexadecimal é um sistema de numeração de base 16, que utiliza os dígitos de 0 a 9 e as letras de A a F para representar valores.
# # O prefixo 0x indica que o número é hexadecimal.
# # Exemplo: 0x1A representa o número 26 em decimal.
nome = 'Jhonnatan'
preco = 1000.9434393
variavel = '%s, o preço total foi de R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (15, 15))