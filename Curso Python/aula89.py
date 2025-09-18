"""Exemplos didáticos: dir, hasattr, getattr e setattr

- dir(obj): lista os atributos e métodos disponíveis no objeto
- hasattr(obj, 'nome'): verifica se o objeto tem o atributo/método
- getattr(obj, 'nome'): obtém o atributo/método; pode receber um valor padrão
- setattr(obj, 'nome', valor): define (ou cria) um atributo dinamicamente

Este arquivo demonstra uso seguro de getattr (checando callable antes de chamar),
uso de default em getattr e um exemplo com uma classe simples.
"""


def demo_string():
    string = '   Luiz   '
    metodo = 'strip'

    print('\n--- Exemplo com string ---')
    # listar alguns métodos/atributos (filtrando privados)
    public_members = [name for name in dir(string) if not name.startswith('__')]
    print('Alguns membros públicos de str:', public_members[:8])

    # checar existência de método
    print("hasattr(string, 'upper') ->", hasattr(string, 'upper'))
    print(f"hasattr(string, '{metodo}') ->", hasattr(string, metodo))

    # obter o método com getattr (sem chamar ainda)
    if hasattr(string, metodo):
        atributo = getattr(string, metodo)
        print('getattr retorna um objeto:', atributo)
        print('É chamável?', callable(atributo))
        # chamar o método somente se for chamável
        if callable(atributo):
            print('Resultado de', metodo, '()->', atributo())
    else:
        # usar terceiro argumento de getattr como valor padrão seguro
        print('Método não existe, valor padrão:', getattr(string, metodo, 'método-inexistente'))

    # usar getattr com um atributo que não existe -> retorna None (ou outro default)
    print("getattr(string, 'foo', 'default') ->", getattr(string, 'foo', 'default'))


def demo_classe():
    print('\n--- Exemplo com classe customizada ---')

    class Pessoa:
        def __init__(self, nome):
            self.nome = nome

        def saudar(self, saudacao='Oi'):
            return f"{saudacao}, eu sou {self.nome}"

    p = Pessoa('Luiz')

    # verificar atributos existentes
    print('hasattr(p, "nome") ->', hasattr(p, 'nome'))
    print('getattr(p, "nome") ->', getattr(p, 'nome'))

    # adicionar atributo dinamicamente
    setattr(p, 'idade', 30)
    print('Atributos via __dict__ ->', p.__dict__)
    print('getattr(p, "idade") ->', getattr(p, 'idade'))

    # obter método dinamicamente e chamá-lo
    metodo = 'saudar'
    if hasattr(p, metodo):
        fn = getattr(p, metodo)
        print('Método encontrado, é chamável?', callable(fn))
        if callable(fn):
            print('Chamada:', fn('Olá'))

    # usar getattr com default quando atributo não existe
    print("getattr(p, 'endereco', 'não definido') ->", getattr(p, 'endereco', 'não definido'))


if __name__ == '__main__':
    demo_string()
    demo_classe()
    print('\nDica rápida: use dir() para explorar objetos; use getattr com default',
          'e cheque callable() antes de invocar o resultado de getattr.')