"""Introdução a generator functions em Python.

Este arquivo mostra exemplos e explicações didáticas sobre:
- generator functions (def com yield)
- generator expressions (parênteses)
- consumo com next() e for
- limitando consumo de um generator grande com itertools.islice
- generator que recebe valores via send()

Observação: evitar imprimir milhões de valores em demos; usamos islice para
mostrar apenas parte do fluxo quando demonstramos generators grandes.
"""

from itertools import islice


def generator(start=0, maximum=10):
    """Gera inteiros a partir de start até maximum-1.

    Note que usar `return` dentro de um generator encerra a iteração e gera
    StopIteration. O yield produz valores de forma preguiçosa (lazy).
    """
    n = start
    while True:
        yield n
        n += 1

        if n >= maximum:
            # return encerra o generator (equivalente a raise StopIteration)
            return


def generator_recebe_valor():
    """Exemplo de generator que recebe valores via send().

    Quando usamos `valor = yield something`, o next() inicial avança até o
    primeiro yield e devolve o lado direito; enviar com send(x) faz com que
    o yield retorne x dentro do generator.
    """
    received = yield 'pronto'
    # received conterá o valor passado por send()
    yield f'Recebi: {received}'


if __name__ == '__main__':
    print('\n--- Exemplo 1: generator simples (pequeno) ---')
    g = generator(start=0, maximum=5)
    for x in g:
        print(x)

    print('\n--- Exemplo 2: generator expression ---')
    # expressão geradora (lazy) - sem criar lista na memória
    ge = (n * n for n in range(6))
    print('type(ge)=', type(ge))
    print('valores:', list(ge))

    print('\n--- Exemplo 3: consumir parcialmente um generator grande ---')
    big = generator(start=0, maximum=1000000)
    # mostrar apenas os 5 primeiros valores usando islice
    for v in islice(big, 5):
        print(v)

    print('\n--- Exemplo 4: uso de next() e StopIteration ---')
    g2 = generator(start=10, maximum=13)
    print(next(g2))
    print(next(g2))
    print(next(g2))
    try:
        print(next(g2))
    except StopIteration:
        print('StopIteration levantado - generator esgotado')

    print('\n--- Exemplo 5: generator que recebe valor via send() ---')
    gr = generator_recebe_valor()
    # inicializa o generator até o primeiro yield
    primeiro = next(gr)
    print('primeiro yield ->', primeiro)
    # envia um valor para o generator; isso faz com que o yield anterior
    # retorne esse valor dentro do generator
    segundo = gr.send('Olá do send')
    print('segundo yield ->', segundo)

    print('\nDica: generators são úteis para processamento de streams, leituras de '\
          'arquivos grandes e pipelines onde não se deseja carregar tudo na memória.')