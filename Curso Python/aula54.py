"""
Exercicio

Faça uma lista de compras com listas, na qual o usuário deverá ter 
a possibilidade de inserir, remover e listar da sua lista e não permita
que o programa quebre com erros de índice inexistentes na lista.
"""

# Inicializa a lista de compras
lista_compras = []

while True:
    print("\nEscolha uma opção:")
    print("1 - Inserir item")
    print("2 - Remover item")
    print("3 - Listar itens")
    print("4 - Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        item = input("Digite o item que deseja adicionar: ")
        lista_compras.append(item)  # Adiciona o item à lista
        print(f"'{item}' foi adicionado à lista.")

    elif opcao == "2":
        if lista_compras:  # Verifica se a lista não está vazia
            try:
                indice = int(input("Digite o índice do item que deseja remover: "))
                item_removido = lista_compras.pop(indice)  # Remove o item pelo índice
                print(f"'{item_removido}' foi removido da lista.")
            except (ValueError, IndexError):
                print("Índice inválido. Tente novamente.")
        else:
            print("A lista de compras está vazia. Não há itens para remover.")

    elif opcao == "3":
        if lista_compras:  # Verifica se a lista não está vazia
            print("\nItens na lista de compras:")
            for i, item in enumerate(lista_compras):
                print(f"{i} - {item}")
        else:
            print("A lista de compras está vazia.")

    elif opcao == "4":
        print("Saindo do programa. Até mais!")
        break

    else:
        print("Opção inválida. Tente novamente.")
