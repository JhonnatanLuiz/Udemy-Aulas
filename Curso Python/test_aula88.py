import pytest # type: ignore

from aula88 import falsy


@pytest.mark.parametrize("value,expected", [
    ([], 'falsy'),
    ({}, 'falsy'),
    (set(), 'falsy'),
    ((), 'falsy'),
    ('', 'falsy'),
    (0, 'falsy'),
    (0.0, 'falsy'),
    (None, 'falsy'),
    (False, 'falsy'),
    (range(0), 'falsy'),

    ([1], 'truthy'),
    ({'a': 1}, 'truthy'),
    ({0}, 'truthy'),
    ((0,), 'truthy'),
    ('0', 'truthy'),
    (1, 'truthy'),
    (-0.5, 'truthy'),
    (True, 'truthy'),
    (range(1), 'truthy'),
])
def test_falsy_param(value, expected):
    assert falsy(value) == expected


def test_custom_bool():
    class AlwaysFalsy:
        def __bool__(self):
            return False

    assert falsy(AlwaysFalsy()) == 'falsy'


def test_tuple_immutable():
    t = (1, 2)
    with pytest.raises(TypeError):
        t[0] = 10
