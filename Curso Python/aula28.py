"""
Exercício
Peça ao usuário para digitar o seu nome
Peça para o usuário para digitar a sua idade
Se nome e idade forem digitados corretamente, imprima na tela:
Seu nome é {nome}
Seu nome invertido é {nome invertido}
Seu nome contém (ou não) espaços
Seu nome tem {n} letras
A primeira letra do seu nome é {primeira letra}
A última letra do seu nome é {última letra}
Se nada for digitado em nome ou idade, imprima:
Desculpe, você não digitou o nome ou a idade
    """
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
if nome == '' or idade == '':
    print('Desculpe, você não digitou o nome ou a idade')
else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'Seu nome contém (ou não) espaços: {" " in nome}')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')