"""Exemplos didáticos de try, except, else e finally em Python.

Este arquivo demonstra:
- Tratamento básico de exceções com try/except/else/finally
- Captura de múltiplos tipos de exceção
- Acesso às informações da exceção (nome da classe, mensagem)
- Uso de raise para lançar exceções
- Comparação entre try/finally manual e context manager (with)
- Exceções customizadas

Referência: https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
"""


def exemplo_basico():
    """Exemplo básico: ZeroDivisionError com else e finally."""
    print('\n--- Exemplo Básico ---')
    try:
        print('ABRIR ARQUIVO (simulação)')
        # Forçar ZeroDivisionError (expressão intencional para causar erro)
        _ = 8 / 0  # Atribuir a _ para evitar warning de expressão não usada
    except ZeroDivisionError as e:
        print(f'Classe da exceção: {e.__class__.__name__}')
        print(f'Mensagem: {e}')
        print('DIVIDIU POR ZERO')
    except IndexError:
        print('IndexError capturado')
    except (NameError, ImportError):
        print('NameError ou ImportError')
    else:
        print('Não deu erro (else executado)')
    finally:
        print('FECHAR ARQUIVO (sempre executado)')


def exemplo_multiplas_excecoes():
    """Demonstra captura de diferentes tipos de erro."""
    print('\n--- Múltiplas Exceções ---')

    # Teste 1: IndexError
    try:
        lista = [1, 2]
        print('Acessando lista[5]:', lista[5])
    except IndexError as e:
        print(f'IndexError: {e}')
    finally:
        print('Finalizado teste 1')

    # Teste 2: NameError
    try:
        # Intencionalmente usar variável não definida para demonstrar NameError
        print(variavel_nao_definida)  # type: ignore
    except NameError as e:
        print(f'NameError: {e}')
    finally:
        print('Finalizado teste 2')


def exemplo_raise():
    """Exemplo de uso de raise para lançar exceções."""
    print('\n--- Uso de raise ---')

    def dividir(a, b):
        if b == 0:
            raise ZeroDivisionError('Divisão por zero não permitida!')
        return a / b

    try:
        resultado = dividir(10, 0)
        print(f'Resultado: {resultado}')
    except ZeroDivisionError as e:
        print(f'Exceção lançada: {e}')
    else:
        print('Divisão realizada com sucesso')


def exemplo_context_manager():
    """Comparação entre try/finally manual e context manager."""
    print('\n--- Context Manager vs try/finally ---')

    # Simulação de arquivo com try/finally
    print('Usando try/finally:')
    arquivo = None
    try:
        arquivo = open('temp.txt', 'w', encoding='utf-8')
        arquivo.write('Conteúdo de teste\n')
        print('Arquivo escrito com sucesso')
    except Exception as e:
        print(f'Erro ao escrever: {e}')
    finally:
        if arquivo:
            arquivo.close()
            print('Arquivo fechado manualmente')

    # Usando context manager (with) - forma preferida
    print('\nUsando with (context manager):')
    try:
        with open('temp.txt', 'r', encoding='utf-8') as f:
            conteudo = f.read()
            print(f'Conteúdo lido: {conteudo.strip()}')
        # Arquivo fechado automaticamente aqui
        print('Arquivo fechado automaticamente')
    except FileNotFoundError:
        print('Arquivo não encontrado')
    except Exception as e:
        print(f'Erro: {e}')


def exemplo_excecao_customizada():
    """Exemplo de criação e uso de exceção customizada."""
    print('\n--- Exceção Customizada ---')

    class ValorInvalidoError(Exception):
        """Exceção para valores inválidos."""
        def __init__(self, valor, mensagem="Valor inválido"):
            self.valor = valor
            self.mensagem = mensagem
            super().__init__(self.mensagem)

    def validar_idade(idade):
        if not isinstance(idade, int):
            raise ValorInvalidoError(idade, "Idade deve ser um inteiro")
        if idade < 0 or idade > 150:
            raise ValorInvalidoError(idade, "Idade deve estar entre 0 e 150")
        return idade

    try:
        idade = validar_idade(-5)
        print(f'Idade válida: {idade}')
    except ValorInvalidoError as e:
        print(f'Erro customizado: {e}')
        print(f'Valor problemático: {e.valor}')


def executar_todos_exemplos():
    """Executa todos os exemplos em sequência."""
    exemplo_basico()
    exemplo_multiplas_excecoes()
    exemplo_raise()
    exemplo_context_manager()
    exemplo_excecao_customizada()


if __name__ == '__main__':
    executar_todos_exemplos()