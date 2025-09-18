'''
# Aula 41 - Iterando strings com while

# Este código encontra a letra que mais aparece em uma frase e exibe o resultado.
# 1. A variável 'frase' contém a string que será analisada.
# 2. O loop 'while' percorre cada caractere da string 'frase'.
# 3. Se o caractere atual for um espaço, ele é ignorado com 'continue'.
# 4. A função 'count' é usada para contar quantas vezes o caractere atual aparece na string.
# 5. Se a quantidade atual for maior que a maior quantidade registrada, as variáveis
#    'qtd_apareceu_mais_vezes' e 'letra_apareceu_mais_vezes' são atualizadas.
# 6. Após o loop, o programa exibe a letra que mais apareceu e sua quantidade.
'''
frase = 'O Python é uma linguagem de programação multi-paradigma, de tipagem dinâmica e forte, O Python foi criado por Guido van Rossum e lançado em 1991.'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    
    i += 1 

print(
        'A letra que mais apareceu foi '
        f'{letra_apareceu_mais_vezes} que apareceu '
        f'{qtd_apareceu_mais_vezes} x'
    )