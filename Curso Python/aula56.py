"""
aula 56 - split e join com list e str
# # split() é um método de string que divide uma string em uma lista, usando um delimitador especificado (por padrão, espaço em branco).
# # join() é um método de string que junta os elementos de uma lista em uma única string, usando um delimitador especificado.
# # split() e join() são frequentemente usados juntos para dividir uma string em uma lista e depois juntar os elementos da lista em uma nova string.
# # split() e join() são métodos de string que permitem dividir e juntar strings, respectivamente.
# # split() divide uma string em uma lista de substrings, enquanto join() junta uma lista de strings em uma única string.
# # strip() é um método de string que remove espaços em branco do início e do fim de uma string.
# # lstrip() remove espaços em branco do início de uma string, enquanto rstrip() remove espaços em branco do fim de uma string.
"""

frase = 'O rato roeu a roupa do rei de Roma'
lista_frases_cruas = frase.split(',')
 
lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
     lista_frases.append(lista_frases_cruas[i].strip())
     
frases_unidas = ', '.join(lista_frases)
print(frases_unidas) 