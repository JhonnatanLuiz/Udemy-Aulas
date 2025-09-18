"""
# Aula 45 - iteraveis e iteradores
Iterável: str, range, list, tuple, set, dict, etc.
Iterador: Quem sabe entregar um valor por vez, como o for.
next: Pega o próximo valor do iterador.
iter: me entrega seu iterador.

"""
texto = 'Luiz'
"""iterador = iter(texto)

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration: 
        break """
for letra in texto:
    print(letra)


