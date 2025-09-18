# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0
for pergunta in perguntas:
    print(pergunta['Pergunta'])
    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i}) {opcao}')
    resposta_usuario = input('Escolha uma opção: ')
    # Corrigido: verifica se a entrada é um índice válido
    if resposta_usuario.isdigit():
        indice = int(resposta_usuario)
        if 0 <= indice < len(pergunta['Opções']):
            if pergunta['Opções'][indice] == pergunta['Resposta']:
                print('Acertou!')
                acertos += 1
            else:
                print('Errou!')
        else:
            print('Opção inválida!')
    else:
        print('Entrada inválida!')
    print()

print(f'Você acertou {acertos} de {len(perguntas)} perguntas.')
# Explicação:
# O sistema percorre cada pergunta, exibe as opções, recebe a resposta do usuário e informa se acertou ou errou.
# Ao final, mostra o total de acertos.