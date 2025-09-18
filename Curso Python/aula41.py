'''
# Aula 41 - while e else
# O comando while é um loop que executa enquanto a condição for verdadeira
# O comando else é executado quando o loop termina normalmente, sem interrupções

'''
string = 'valor qualquer'

i = 0
while i < len(string):
    letra = string[i]
    if letra == '':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string') # O loop while foi executado normalmente, sem interrupções
    print('Saí do loop while')
# O loop while foi executado normalmente, sem interrupções