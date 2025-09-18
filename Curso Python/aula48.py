"""
Aula 48 - Listas em Python
Listas são estruturas de dados que permitem armazenar múltiplos valores em uma única variável.
Listas são mutáveis, ou seja, podem ser alteradas após a criação.
Listas podem conter diferentes tipos de dados, como números, strings, listas aninhadas, etc.
Listas são definidas usando colchetes [] e os elementos são separados por vírgulas.
Conhecimento reutilizáveis - índices
Listas são indexadas, ou seja, cada elemento tem um índice associado a ele.
Fatiamento de listas permite acessar uma parte da lista usando a notação [início:fim].
Métodos de listas incluem append(), insert(), remove(), pop(), sort(), reverse(), entre outros.
Create Read Update Delete (CRUD) - Listas
Create: Criar uma lista vazia ou com elementos iniciais.
Read: Acessar elementos da lista usando índices ou fatiamento.
Update: Alterar elementos da lista usando índices.
Delete: Remover elementos da lista usando métodos como remove() ou pop().
"""

"""# Definição de uma string com 5 caracteres
string = "ABCDE" #5 caracteres

# Criação de uma lista com diferentes tipos de dados
lista = [123, True, 'Jhonnatan', 1.5, []]

# Alteração do elemento na posição -3 (índice negativo conta de trás para frente)
lista[-3] = 'Luiz'

# Impressão da lista atualizada
print(lista)

# Impressão do elemento na posição 2 da lista e seu tipo
print(lista[2], type(lista[2]))"""

# Criação de uma lista com valores inteiros
#lista = [10, 20, 30, 40, 50]

# Exemplos de operações comentadas:
# lista[2] = 300  # Alteração do valor no índice 2
# del lista[2]    # Remoção do elemento no índice 2
# print(lista)    # Impressão da lista
# print(lista[2]) # Impressão do elemento no índice 2

# Adiciona o valor 58 ao final da lista
#lista.append(58)

# Remove o último elemento da lista
#lista.pop()

# Adiciona os valores 69 e 78 ao final da lista
#lista.append(69)
#lista.append(78)

# Remove o elemento no índice 5 e armazena em uma variável
#ultimo_valor = lista.pop(5)

# Impressão da lista atualizada e do valor removido
#print(lista, 'removido,', ultimo_valor)

"""lista = [10, 20, 30, 40, 50]
lista.append('Jhonnatan')
nome = lista.pop()
lista.append(123)
del lista[0]
lista.insert(2, 1)
print(lista)"""

"""lista_a = [10, 20, 30, 40, 50]
lista_b = [60, 70, 80, 90, 100]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b)
print(lista_a)"""

"""Cuidado com dados mutáveis
==> copiado o valor (imutáveis)
==> aponta para o mesmo objeto (mutáveis)"""

"""lista_a = ['Jhonnatan', 'Luiz', 123, 1.5, True]
lista_b = lista_a.copy()  # Faz uma cópia da lista_a

lista_a[0] = 'Qualquer coisa'  # Altera o primeiro elemento da lista_a
print(lista_a)  # Imprime a lista_a alterada
print(lista_b)  # Imprime a lista_b (cópia) sem alterações
# lista_b[0] = 'Outro nome'  # Altera o primeiro elemento da lista_b"""

