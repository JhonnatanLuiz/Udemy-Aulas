# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Exemplos de valores vazios/zeros (falsy) e não vazios (truthy)
# Tipos mutáveis: list, dict, set, bytearray
# Tipos imutáveis: tuple, str, int, float, bool, range, bytes

# --- exemplos iniciais (vazios / zero) ---
lista = []                  # lista vazia -> falsy
dicionario = {}             # dicionário vazio -> falsy
conjunto = set()            # set vazio -> falsy
tupla = ()                  # tupla vazia -> falsy
string = ''                 # string vazia -> falsy
inteiro = 0                 # zero -> falsy (note o nome corrigido)
flutuante = 0.0             # zero float -> falsy
nada = None                 # None -> falsy
falso = False               # False -> falsy
intervalo = range(0)        # range vazio -> falsy


def falsy(valor):
    """Retorna 'falsy' se o valor for considerado falso em contexto booleano,
    caso contrário retorna 'truthy'.

    Observação: em Python, objetos vazios (len == 0), 0, 0.0, None e False
    são avaliados como False; a maioria dos outros objetos é True por padrão.
    """
    return 'falsy' if not valor else 'truthy'


if __name__ == '__main__':
    # Imprime os exemplos iniciais
    print('--- Exemplos base (vazios / zero) ---')
    print(f'lista (vazia)= {lista!r} ->', falsy(lista))
    print(f'dicionario (vazio)= {dicionario!r} ->', falsy(dicionario))
    print(f'conjunto (vazio)= {conjunto!r} ->', falsy(conjunto))
    print(f'tupla (vazia)= {tupla!r} ->', falsy(tupla))
    print(f'string (vazia)= {string!r} ->', falsy(string))
    print(f'inteiro = {inteiro!r} ->', falsy(inteiro))
    print(f'flutuante = {flutuante!r} ->', falsy(flutuante))
    print(f'nada = {nada!r} ->', falsy(nada))
    print(f'falso = {falso!r} ->', falsy(falso))
    print(f'intervalo = {intervalo!r} ->', falsy(intervalo))

    # --- exemplos não vazios (truthy) ---
    print('\n--- Exemplos não vazios / truthy ---')
    lista2 = [1, 2]
    dicionario2 = {'a': 1}
    conjunto2 = {0}
    tupla2 = (0,)
    string2 = '0'            # string com caractere -> truthy
    inteiro2 = 1
    flutuante2 = -0.5
    verdadeiro = True
    intervalo2 = range(1)    # range com um elemento -> truthy

    print(f'lista2 = {lista2!r} ->', falsy(lista2))
    print(f'dicionario2 = {dicionario2!r} ->', falsy(dicionario2))
    print(f'conjunto2 = {conjunto2!r} ->', falsy(conjunto2))
    print(f'tupla2 = {tupla2!r} ->', falsy(tupla2))
    print(f'string2 = {string2!r} ->', falsy(string2))
    print(f'inteiro2 = {inteiro2!r} ->', falsy(inteiro2))
    print(f'flutuante2 = {flutuante2!r} ->', falsy(flutuante2))
    print(f'verdadeiro = {verdadeiro!r} ->', falsy(verdadeiro))
    print(f'intervalo2 = {intervalo2!r} ->', falsy(intervalo2))

    # --- mutabilidade vs imutabilidade ---
    print('\n--- Mutabilidade / Imutabilidade ---')
    # listas (mutáveis) podem ser alteradas em lugar
    lista_mutavel = [1, 2]
    print('antes lista_mutavel =', lista_mutavel)
    lista_mutavel.append(3)
    print('depois lista_mutavel =', lista_mutavel)

    # tuplas (imutáveis) não permitem atribuição direta
    t = (1, 2)
    print('tupla t =', t)
    # Para "alterar" um elemento é necessário criar um novo tuple,
    # já que tuples são imutáveis (não suportam __setitem__).
    t_nova = (10,) + t[1:]
    print('novo tuple criado =', t_nova)

    # Edge-case: objetos customizados são truthy a menos que definam __bool__ ou __len__
    class AlwaysFalsy:
        def __bool__(self):
            return False

    obj = AlwaysFalsy()
    print('\nobjeto customizado com __bool__ ->', falsy(obj))

    # Observações finais (resumo rápido):
    print('\nResumo: valores como [], {}, (), "", 0, 0.0, None e False são falsy;',
          'quase todo o resto é truthy por padrão.')