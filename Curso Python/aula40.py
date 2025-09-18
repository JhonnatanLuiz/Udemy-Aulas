'''
aula 40 - Calculadora com while
'''

import math

# Função para exibir o menu da calculadora
historico = []

while True:
    print('Menu:')
    print('1. Fazer um cálculo')
    print('2. Ver histórico')
    print('3. Sair')
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        numero_1 = input('Digite um número: ')
        numero_2 = input('Digite outro número: ')

        # Substitua vírgulas por pontos para aceitar entradas como "1,5"
        numero_1 = numero_1.replace(',', '.')
        numero_2 = numero_2.replace(',', '.')

        operador = input('Digite o operador (+-/*): ')

        # Validação dos números
        try:
            num_1_float = float(numero_1)
            num_2_float = float(numero_2)
        except ValueError:
            print('Um ou ambos os números digitados são inválidos.')
            continue

        # Validação do operador
        operadores_permitidos = '+-/*'
        if operador not in operadores_permitidos or len(operador) > 1:
            print('Operador inválido. Digite apenas um operador válido (+, -, *, /).')
            continue

        # Realizar o cálculo
        if operador == '+':
            resultado = num_1_float + num_2_float
        elif operador == '-':
            resultado = num_1_float - num_2_float
        elif operador == '*':
            resultado = num_1_float * num_2_float
        elif operador == '/':
            if num_2_float == 0:
                print('Erro: Divisão por zero não é permitida.')
                continue
            resultado = num_1_float / num_2_float
        elif operador == '**':
            resultado = num_1_float ** num_2_float
        elif operador == '%':
            resultado = num_1_float % num_2_float
        elif operador == 'sqrt':
            resultado = math.sqrt(num_1_float)

        print(f'O resultado de {num_1_float} {operador} {num_2_float} é: {resultado}')

        historico.append(f'{num_1_float} {operador} {num_2_float} = {resultado}')

        continuar = input('Deseja continuar com o resultado anterior? [s]im: ').lower().startswith('s')
        if continuar:
            numero_1 = str(resultado)
            continue

    elif opcao == '2':
        print('Histórico de cálculos:')
        for item in historico:
            print(item)

    elif opcao == '3':
        # Salvar histórico em um arquivo
        with open('historico_calculadora.txt', 'w') as arquivo:
            for item in historico:
                arquivo.write(item + '\n')
        break

    else:
        print('Opção inválida.')