# Operadores lógicos:
# # and (e), or (ou), not (não)
# # and: Retorna True se ambas as condições forem verdadeiras.
# # or: Retorna True se pelo menos uma das condições for verdadeira.
# # not: Inverte o valor lógico da condição (True se torna False e vice-versa).
# None: Representa a ausência de valor ou um valor nulo.

"""entrada = input('[E]ntrar ou [S]air? ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

#print(True and False and True)
#print(True and 0 and True)"""

idade = 25
tem_carteira = True

# Ambas as condições são True?
pode_dirigir = idade >= 18 and tem_carteira

print(f"Pode dirigir? {pode_dirigir}") # Output: Pode dirigir? True

idade2 = 16
tem_carteira2 = True

# idade2 >= 18 é False. A segunda condição (tem_carteira2) não será avaliada.
pode_dirigir2 = idade2 >= 18 and tem_carteira2

print(f"Pode dirigir 2? {pode_dirigir2}") # Output: Pode dirigir 2? False
