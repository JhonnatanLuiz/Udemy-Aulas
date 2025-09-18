""" Formatação básica de strings
s- string
d- inteiro
f- float
x- hexadecimal
X- hexadecimal (letras maiúsculas)
e- exponencial
(Caractere) (><^) (quantidade) (tipo)
# >- Alinhamento à direita (padrão)
# < - Alinhamento à esquerda
# ^ - Alinhamento centralizado
= Força o sinal de número a aparecer antes do espaço em branco (apenas para números)
Sinal de mais ou menos: + ou -
Exemplo: %10s - Alinha à direita em 10 espaços
Conversion flags: 
!r - Representação oficial (repr)
!s - Representação de string (str)
!a - Representação de string ASCII (ascii)
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel:>10}')
print(f'{variavel:<10}')
print(f'{variavel:^10}')
print(f'{1000.9434393:.2f}')
print(f' O hexadecimal de 255 é {255:X}')
print(f'{variavel!r}')