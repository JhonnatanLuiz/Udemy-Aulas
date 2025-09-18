"""Mais detalhes sobre Iterables e Iterators (Iteráveis e Iteradores)

Conceitos rápidos (em Português didático):
- Iterable (iterável): um objeto que pode retornar um iterator; tipicamente
  tem um método __iter__() que retorna um iterator. Exemplos: list, tuple, str,
  dict, set, range, arquivos abertos, geradores.
- Iterator (iterador): um objeto que representa um fluxo de dados; implementa
  __next__() (ou next() em Python 2) e __iter__() que retorna ele mesmo. Chamar
  next(iterator) retorna o próximo item ou levanta StopIteration quando
  esgotado.

Em Python, um for usa internamente iter() para obter um iterator e next() para
consumir valores até StopIteration. Geradores (funções com yield) criam iterators
de forma conveniente.

Este arquivo contém exemplos curtos e comentários para experimentação.
"""

from collections.abc import Iterable, Iterator


def contador(n):
	"""Generator simples que conta de 0 até n-1."""
	i = 0
	while i < n:
		yield i
		i += 1


class Contador:
	"""Iterator manual que produz 0..limite-1 e mantém estado interno."""
	def __init__(self, limite):
		self.limite = limite
		self.atual = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self.atual < self.limite:
			valor = self.atual
			self.atual += 1
			return valor
		raise StopIteration


def exemplo_basico():
	print('\n--- Exemplo básico: list (iterable) e iter() -> iterator ---')
	numeros = [10, 20, 30]
	print('numeros é Iterable?', isinstance(numeros, Iterable))

	it = iter(numeros)  # cria um iterator a partir do iterável
	print('it é Iterator?', isinstance(it, Iterator))
	print('next(it) ->', next(it))
	print('next(it) ->', next(it))
	print('next(it) ->', next(it))
	try:
		print('next(it) ->', next(it))
	except StopIteration:
		print('Iterator esgotado (StopIteration)')


def exemplo_for_consumo():
	print('\n--- Como for consome um iterable ---')
	texto = 'AB'
	# for internamente: it = iter(texto); while True: try: x = next(it)
	# em cada iteração
	for ch in texto:
		print('caractere:', ch)


def exemplo_generator():
	print('\n--- Generator (yield) ---')
	gen = contador(3)
	print('gen é Iterable?', isinstance(gen, Iterable))
	print('gen é Iterator?', isinstance(gen, Iterator))
	print('itens gerados:')
	for x in gen:
		print(' ->', x)


def exemplo_classe_iterator():
	print('\n--- Implementando um Iterator manualmente ---')
	c = Contador(3)
	print('Contador é Iterable?', isinstance(c, Iterable))
	print('Contador é Iterator?', isinstance(c, Iterator))
	print('Valores do contador:')
	for v in c:
		print(' ->', v)


def observacoes():
	print('\n--- Observações e boas práticas ---')
	print('- Iteráveis podem ser percorridos várias vezes (ex: list),\n  pois __iter__ cria um novo iterator a cada vez.')
	print("- Iteradores normalmente são consumidos uma vez; depois disso\n  estão esgotados (ex: generator e objetos iterator custom).")
	print('- Se precisar reiniciar, crie um novo iterator chamando iter(iterable) novamente.')


if __name__ == '__main__':
	exemplo_basico()
	exemplo_for_consumo()
	exemplo_generator()
	exemplo_classe_iterator()
	observacoes()
