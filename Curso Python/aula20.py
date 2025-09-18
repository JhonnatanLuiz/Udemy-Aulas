primeiro_valor = input('Digite um número: ')
segundo_valor = input('Digite outro número: ')

try:
    primeiro_valor = int(primeiro_valor)
    segundo_valor = int(segundo_valor)

    if primeiro_valor > segundo_valor:
        print('O primeiro valor é maior.')
    elif segundo_valor > primeiro_valor:
        print('O segundo valor é maior.')
    else:
        print('Os dois valores são iguais.')
except Exception:
    print('Não foi possivel converter os valores para números inteiros.')
