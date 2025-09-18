"""
Exercício
Faça um jogo para o usuário adivinhar qual a palavra secreta.
você vai propor uma palavra secreta qualquer e vai dar a possibilidade
para o usuário digitar apenas uma letra.
Quando o usuário digitar uma letra, você vai conferir se a letra está
na palavra secreta.
Se a letra digitada estiver na palavra secreta; exiba a letra;
Se a letra digitada não estiver na palavra secreta, exiba *.
Faça a contagem de tentativas do seu usuário.
"""

# Palavra secreta definida pelo programa
palavra_secreta = 'perfume'
# Variável para armazenar as tentativas do usuário
tentativas = 0
# Variável para armazenar as letras acertadas pelo usuário
letras_acertadas = ''

print('Bem-vindo ao jogo de adivinhação!')

while True:
    letra = input('Digite uma letra: ').lower()  # Solicita uma letra ao usuário
    tentativas += 1  # Incrementa o contador de tentativas

    if len(letra) != 1:  # Verifica se o usuário digitou apenas uma letra
        print('Por favor, digite apenas uma letra.')
        continue

    if letra in palavra_secreta:  # Verifica se a letra está na palavra secreta
        letras_acertadas += letra
        print(f'Boa! A letra "{letra}" está na palavra secreta.')
    else:
        print(f'A letra "{letra}" não está na palavra secreta.')

    # Exibe a palavra com as letras acertadas e * para as letras não descobertas
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(f'Palavra: {palavra_formada}')

    # Verifica se o usuário descobriu a palavra secreta
    if palavra_formada == palavra_secreta:
        print(f'Parabéns! Você descobriu a palavra secreta "{palavra_secreta}" em {tentativas} tentativas.')
        break
