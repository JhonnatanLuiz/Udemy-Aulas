# Operações condicionais são usadas para tomar decisões com base em condições específicas. 
# Elas permitem que o programa execute diferentes blocos de código dependendo do resultado de uma condição. 
# As operações condicionais mais comuns são: if, elif e else.
# A estrutura básica de uma operação condicional é a seguinte:
# if condição:
#     # bloco de código a ser executado se a condição for verdadeira
# elif outra_condição:
#     # bloco de código a ser executado se a outra condição for verdadeira
# else:
#     # bloco de código a ser executado se nenhuma das condições anteriores for verdadeira
entrada = input('Você quer "entrar" ou "sair"?')
if entrada == "entrar":
    print("Você entrou")
    print("Bem-vindo!")
elif entrada == "sair":
    print("Você saiu")
else:
    print("Opção inválida")
    print("Tente novamente")