"""
    Aula 27 - Fatiamento de Strings
    Fatiamento de strings é uma técnica que permite extrair partes de uma string,
    utilizando índices para especificar o início e o fim do trecho desejado.
    O fatiamento é feito utilizando a notação [início:fim:passo], onde:
    - início: índice onde o fatiamento começa (inclusivo)
    - fim: índice onde o fatiamento termina (exclusivo)
    Se omitir o final, o fatiamento vai até o final da string.
    Função len() retorna o tamanho da string.
"""
variavel = 'Ola mundo!'
print((variavel)[0:len(variavel):1])