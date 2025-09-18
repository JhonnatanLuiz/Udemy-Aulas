"""
aula 39 - Iterando strings com while
# Iterando strings com while
Iterando strings com while significa que você está percorrendo 
cada caractere da string um por um, e executando um bloco de código 
para cada caractere.
Isso pode ser útil quando você precisa realizar operações específicas 
em cada caractere da string,

"""

nome = 'jhonnatan' # String de exemplo
tamanho_do_nome = len(nome) # Calcula o tamanho da string
print(nome) # Exibe a string original
print(tamanho_do_nome) # Exibe o tamanho da string
print(nome[5]) # Exibe o caractere na posição 5

nova_string = ''  # Inicialize a nova string
indice = 0  # Índice inicial

while indice < tamanho_do_nome: # Enquanto o índice for menor que o tamanho da string
    nova_string += nome[indice]  # Adiciona o caractere atual à nova string
    indice += 1  # Incrementa o índice

print(nova_string)  # Exibe a nova string