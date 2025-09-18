"""
Exercícios de fixação - Estruturas condicionais
Exercício 1
Faça um programa que peça ao usuário para digitar um número inteiro e, em seguida, verifique se o número é par ou ímpar.
Se o número for par, exiba uma mensagem informando que o número é par. Caso o usuário não digite um número inteiro, exiba uma mensagem de erro.
# O programa deve continuar pedindo um número até que o usuário digite um número válido.

Exercício 2
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada.
# Exiba "Bom dia" se a hora estiver entre 0 e 11, "Boa tarde" se estiver entre 12 e 17 e "Boa noite" se estiver entre 18 e 23.
# Caso o usuário digite um horário inválido, exiba uma mensagem de erro.
# O programa deve continuar pedindo um horário até que o usuário digite um horário válido.

Exercício 3
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos, escreva "Seu nome é curto".
# Se o nome tiver entre 5 e 6 letras, escreva "Seu nome é normal", maior que 6 escreva "Seu nome é muito grande".
# O programa deve continuar pedindo um nome até que o usuário digite um nome válido.

"""
# Exercicio 1 - Par ou Ímpar

'''def par_ou_impar():
    while True:
        try:
            numero = int(input('Digite um número inteiro: '))
            if numero % 2 == 0:
                print(f'O número {numero} é par.')
            else:
                print(f'O número {numero} é ímpar.')
            break  # Sai do loop após um número válido ser processado
        except ValueError:
            print('Erro: Você não digitou um número inteiro válido. Tente novamente.')

# Chamada da função para executar o exercício
par_ou_impar()'''

# Exercicio 2 - Saudação baseada no horário
'''def saudacao_por_horario():
    while True:
        try:
            horario = int(input('Digite a hora atual (0-23): '))
            if 0 <= horario <= 11:
                print('Bom dia!')
            elif 12 <= horario <= 17:
                print('Boa tarde!')
            elif 18 <= horario <= 23:
                print('Boa noite!')
            else:
                print('Erro: O horário deve estar entre 0 e 23. Tente novamente.')
                continue
            break  # Sai do loop se o horário for válido
        except ValueError:
            print('Erro: Você não digitou um horário válido. Tente novamente.')

# Chamada da função para executar o exercício
saudacao_por_horario()'''

# Exercicio 3 - Tamanho do nome
def tamanho_do_nome():
    while True:
        nome = input('Digite seu primeiro nome: ').strip()
        if not nome.isalpha():
            print('Erro: O nome deve conter apenas letras. Tente novamente.')
            continue

        tamanho = len(nome)
        if tamanho <= 4:
            print('Seu nome é curto.')
        elif 5 <= tamanho <= 6:
            print('Seu nome é normal.')
        else:
            print('Seu nome é muito grande.')
        break  # Sai do loop se o nome for válido

# Chamada da função para executar o exercício
tamanho_do_nome()
