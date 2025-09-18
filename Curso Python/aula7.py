# Variáveis são usadas para armazenar dados temporariamente na memória do computador.
# Elas podem ser criadas usando letras, números e o caractere de sublinhado (_), mas não podem começar com um número.
# PEP 8: É um guia de estilo para escrever código Python de forma legível e consistente.
# numéros e underline (_), mas não podem começar com um número.
# atribuir um valor á um nome de variável
# Uso: nome_variavel = expressão
# snake_case: nomeVariavel
# camelcase: nome_variavel
# Pascalcase: NomeVariavel
nome_completo = "Carlos Silva"
soma_dois_mais_dois = 2 + 2
int_um = bool('1') # conversão implícita de string para int
print(int_um, type(int_um))  # Resultado: 1 <class 'int'>
print(nome_completo, soma_dois_mais_dois)  # Resultado: Carlos Silva 4

nome = 'Carlos'
idade = 30
maior_de_idade = idade >= 18
print('Nome:', nome, 'Idade:', idade) # Resultado: Nome: Carlos Idade: 30
print('É maior de idade?', maior_de_idade)  # Resultado: É maior de idade? True)