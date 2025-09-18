'''
aula 43 - introdução ao for/in- estrutura de repetição para coisas finitas
# Este código percorre uma string e conta quantas vezes cada letra aparece, ignorando espaços.
for = estrutura de repetição para coisas finitas
# 1. A variável 'texto' contém a string que será analisada.
# 2. O loop 'for' percorre cada caractere da string 'texto'.
# 3. Se o caractere atual for um espaço, ele é ignorado com 'continue'.
in = operador que verifica se um elemento está dentro de uma coleção (como uma string ou lista).
# 4. A função 'count' é usada para contar quantas vezes o caractere atual aparece na string.
'''
"""senha_salva = '123456789'
senha_digitada = ''
repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input(f'Digite a senha ({repeticoes}x): ')
    
    repeticoes += 1

    print(repeticoes)
    print('Aquele laço acima pode ter repetições infinitas')"""
texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'{letra}'
    print(letra)
    print(novo_texto + '*')
    