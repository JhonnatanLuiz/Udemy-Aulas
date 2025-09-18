nome = 'Jhonnatan Luiz'
altura = 1.75
peso = 80
imc = peso / altura ** 2

"f-strings" # Formatação de strings com f-strings (Python 3.6+)
# São strings que começam com a letra 'f' ou 'F' e permitem a inclusão de expressões dentro de chaves {}.
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Luiz Otávio tem 1.80 de altura,
# pesa 95 quilos e seu IMC é
# 29.320987654320987