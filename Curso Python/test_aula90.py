from aula90 import contador, Contador


def test_contador_generator():
    gen = contador(3)
    assert hasattr(gen, '__iter__')
    assert hasattr(gen, '__next__')
    assert list(gen) == [0, 1, 2]


def test_contador_class_iterator():
    c = Contador(4)
    assert hasattr(c, '__iter__')
    assert hasattr(c, '__next__')
    assert list(c) == [0, 1, 2, 3]


def test_iterable_reuse():
    data = [1, 2]
    it1 = iter(data)
    it2 = iter(data)
    assert next(it1) == 1
    assert next(it2) == 1


def test_iterator_consumed_once():
    gen = contador(2)
    assert list(gen) == [0, 1]
    # generator should be exhausted now
    assert list(gen) == []
