"""
aula 46 - O que aprendemos com while também funciona no for 
(continue, break, else, etc) 
# for/while/if/else = estruturas de controle de fluxo que permitem 
# executar diferentes blocos de código com base em condições.
"""
for i in range(10):  # Loop externo: i varia de 0 a 9
    if i == 2:  # Verifica se i é igual a 2
        print('i é 2, pulando')  # Mensagem indicando que i é 2
        continue  # Pula para a próxima iteração do loop externo

    if i == 8:  # Verifica se i é igual a 8
        print('i é 8, seu else não vai rodar')  # Mensagem indicando que i é 8
        break  # Interrompe o loop externo

    for j in range(1, 3):  # Loop interno: j varia de 1 a 2
        print(i, j)  # Imprime os valores de i e j
else:  # Executado apenas se o loop externo não for interrompido por um break
    print('For completo com sucesso')  # Mensagem indicando que o loop foi concluído