"""Demonstração organizada de try / except / else / finally.

Este arquivo contém funções que mostram diferentes formas de tratar
exceções em Python, como capturar múltiplos tipos, acessar informações
da exceção, usar else e finally e comparar iteração de exceções.
"""


def exemplo_index_error():
    """Exemplo simples: IndexError ao acessar posição inválida de string."""
    print('\n--- exemplo_index_error ---')
    try:
        print('antes do acesso')
        # forçar IndexError
        print('Linha 1'[1000])
        print('isso não será impresso')
    except IndexError as e:
        print('Capturou IndexError:', e.__class__.__name__)
        print('mensagem:', e)
    finally:
        print('finalmente: cleanup se necessário')


def exemplo_zero_division():
    """Exemplo: ZeroDivisionError e como acessar o objeto de exceção."""
    print('\n--- exemplo_zero_division ---')
    try:
        a = 18
        b = 0
        print('dividindo', a, '/', b)
        c = a / b
    except ZeroDivisionError as e:
        # mostrar nome da classe e mensagem
        print('Capturou:', e.__class__.__name__)
        print('mensagem:', e)
    else:
        # executa quando não houve exceção
        print('Resultado da divisão:', c)
    finally:
        print('finalmente: posso sempre executar isso')


def exemplo_multiple_except():
    """Captura múltiplos tipos de exceção e demonstra mensagem genérica."""
    print('\n--- exemplo_multiple_except ---')
    try:
        # descomente para testar NameError / TypeError / IndexError
        # print(b[0])      # NameError se b não existe or TypeError depending
        # print('Linha 1'[1000])
        a = 18
        b = 0
        c = a / b
    except NameError:
        print('Nome não definido')
    except (TypeError, IndexError) as error:
        print('TypeError ou IndexError capturado ->', error)
    except Exception as error:
        print('Exceção desconhecida:', type(error).__name__, error)
    else:
        print('Sem exceção, c=', c)


def executar_todos():
    """Executa todos os exemplos em sequência."""
    exemplo_index_error()
    exemplo_zero_division()
    exemplo_multiple_except()
    exemplo_raise()
    exemplo_try_finally_recurso()


def exemplo_raise():
    """Exemplo de uso de raise para lançar exceções explicitamente."""
    print('\n--- exemplo_raise ---')
    try:
        x = 10
        if x > 5:
            raise ValueError('x é maior que 5 — erro intencional')
    except ValueError as e:
        print('Capturei ValueError:', e)


def exemplo_try_finally_recurso():
    """Exemplo de try...finally para garantir fechamento de recurso (arquivo).

    Também mostramos o uso de `with` que é a forma preferida em Python.
    """
    print('\n--- exemplo_try_finally_recurso ---')
    filename = 'temp_exemplo.txt'
    # criar um arquivo temporário pequeno
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('linha1\nlinha2\n')

    # abrir sem with e garantir fechamento com finally
    f = open(filename, 'r', encoding='utf-8')
    try:
        data = f.read()
        print('conteúdo lido (try/finally):')
        print(data.strip())
    finally:
        f.close()
        print('arquivo fechado via finally')

    # usar with (melhor prática)
    with open(filename, 'r', encoding='utf-8') as f2:
        print('conteúdo lido (with):')
        print(f2.read().strip())

    # remover arquivo temporário
    try:
        import os
        os.remove(filename)
    except Exception:
        pass


if __name__ == '__main__':
    executar_todos()
