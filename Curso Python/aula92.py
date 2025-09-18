"""Exemplos de `yield from` (delegação de generators).

`yield from <iterable>` delega parte da iteração para outro iterable/generator.
Vantagens: encaminha automaticamente valores enviados (send), exceções
(throw) e captura o valor de retorno do subgenerator (StopIteration.value) em
uma variável quando usado em Python 3.3+ (PEP 380).

Este arquivo demonstra:
- delegação simples com `yield from`
- captura do valor retornado por um subgenerator usando `return`
- comparação com iteração manual (sem `yield from`)
"""


def gen1():
    print('COMEÇOU GEN1')
    yield 1
    yield 2
    yield 3
    print('ACABOU GEN1')


def gen3():
    print('COMEÇOU GEN3')
    yield 10
    yield 20
    yield 30
    print('ACABOU GEN3')


def gen2(gen=None):
    """Generator que delega para outro generator opcional via `yield from`.

    Se `gen` for fornecido, `yield from gen` vai iterar sobre ele, repassando
    valores e comportamento (send/throw) para o subgenerator.
    """
    print('COMEÇOU GEN2')
    if gen is not None:
        # delega toda a iteração ao generator/iterable passado
        yield from gen
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN2')


def gen_with_return():
    """Subgenerator que retorna um valor ao terminar (via return).

    Em Python, `return value` dentro de um generator causa StopIteration(value).
    Quando usado com `yield from`, o valor pode ser capturado pela delegação.
    """
    print('COMEÇOU gen_with_return')
    yield 'a'
    yield 'b'
    print('RETORNANDO valor do subgenerator')
    return 42


def delegador_retorno():
    """Mostra como capturar o valor de retorno do subgenerator.

    o `yield from` retorna o valor de StopIteration.value do subgenerator,
    que aqui armazenamos em `ret`.
    """
    print('COMEÇOU delegador_retorno')
    ret = yield from gen_with_return()
    print('valor retornado pelo subgenerator =', ret)
    yield 'fim-delegador'


if __name__ == '__main__':
    print('\n--- delegando gen1 dentro de gen2 ---')
    g1 = gen2(gen1())
    for numero in g1:
        print(numero)

    print('\n--- delegando gen3 dentro de gen2 ---')
    g2 = gen2(gen3())
    for numero in g2:
        print(numero)

    print('\n--- gen2 sem subgenerator ---')
    g3 = gen2()
    for numero in g3:
        print(numero)

    print('\n--- captura de valor retornado por subgenerator usando yield from ---')
    for x in delegador_retorno():
        print('delegador emitted ->', x)

    print('\n--- comparação: delegar (yield from) vs iterar manualmente ---')
    print('delegando (yield from):')
    for x in gen2(gen1()):
        print(' ->', x)

    print('iterando manualmente (sem yield from):')
    def gen_manual(g):
        print('COMEÇOU gen_manual')
        if g is not None:
            for item in g:
                yield item
        yield 4
        yield 5
        yield 6
        print('ACABOU gen_manual')

    for x in gen_manual(gen1()):
        print(' ->', x)