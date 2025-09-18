'''
Introdução ao tipo set em Python (conjuntos)
Conjuntos são ensinados na matemática e representados pelo diagrama de Venn.
Sets em Python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno.
'''

# Criando sets
s1 = set()  # set vazio
s2 = {'Luiz', 1, 2, 3}  # set com dados
s3 = set('Luiz')  # set a partir de string (remove duplicados)
print('s2:', s2)
print('s3:', s3)

# Sets removem valores duplicados automaticamente
duplicados = [1, 2, 2, 3, 3, 3, 4]
set_sem_duplicados = set(duplicados)
print('Sem duplicados:', set_sem_duplicados)

# Não aceitam valores mutáveis, valores sempre únicos, não tem índices, não garantem ordem, são iteráveis

# Métodos úteis:
s = set()
s.add(1)  # Adiciona um elemento
s.update([2, 3, 4])  # Adiciona vários elementos
print('Set após add e update:', s)
s.discard(3)  # Remove o elemento 3 se existir
print('Set após discard:', s)
s.clear()  # Remove todos os elementos
print('Set após clear:', s)

# Operadores úteis:
a = {1, 2, 3}
b = {2, 3, 4}

# União
uniao = a | b
print('União:', uniao)

# Intersecção
interseccao = a & b
print('Interseção:', interseccao)

# Diferença
diferenca = a - b
print('Diferença (a - b):', diferenca)

# Diferença simétrica
dif_simetrica = a ^ b
print('Diferença simétrica:', dif_simetrica)

# Explicação:
# - add: adiciona elemento
# - update: adiciona vários elementos
# - clear: limpa o set
# - discard: remove elemento se existir
# - | união, & interseção, - diferença, ^ diferença simétrica
# - Sets não aceitam valores mutáveis, não têm índices e não garantem ordem