"""
# Aula 31 - A identidade do valor que está na memória
# Identidade = A identidade de um objeto é um valor único que o identifica na memória.
Flag (bandeira) - Marcar um local
is e is not = é pi não é (tipo, valor, identidade)
# O operador is verifica se dois objetos são o mesmo objeto na memória, enquanto o operador == verifica se os valores dos objetos são iguais.
# O operador is é útil para verificar a identidade de objetos, enquanto o operador == é útil para comparar valores.
# O operador is é mais rápido que o operador ==, pois não precisa comparar os valores dos objetos, apenas suas identidades.
id = identidade
# O operador id() retorna o endereço de memória do objeto.
# O operador id() é útil para verificar a identidade de objetos e entender como o Python gerencia a memória.
# O operador id() é útil para depuração e otimização de código, pois permite identificar objetos duplicados ou desnecessários na memória.
# O operador id() é útil para entender como o Python gerencia a memória e otimizar o uso de memória em programas grandes.

"""
'''v1 = 'a'
v2 = 'b'
print(id(v1)) # id = identidade
print(id(v2)) # id = identidade'''

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
