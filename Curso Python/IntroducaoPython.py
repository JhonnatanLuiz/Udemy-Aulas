# INTRODUÇÃO AO PYTHON - GUIA PARA INICIANTES

# 1. PRIMEIROS PASSOS EM PYTHON
# --------------------------

# Seu primeiro programa - Olá, Mundo!
print("Olá, Mundo!")
# Resultado: Olá, Mundo!
# Explicação: A função print() exibe o texto ou valor entre parênteses na tela.

# 2. VARIÁVEIS E TIPOS DE DADOS
# --------------------------

# Declarando variáveis (não é necessário especificar o tipo)
nome = "Maria"      # String (texto)
idade = 25          # Integer (número inteiro)
altura = 1.65       # Float (número decimal)
esta_estudando = True  # Boolean (verdadeiro ou falso)

# Exibindo as variáveis
print(nome)         # Resultado: Maria
print(idade)        # Resultado: 25
print(altura)       # Resultado: 1.65
print(esta_estudando)  # Resultado: True

# Verificando o tipo das variáveis com a função type()
print(type(nome))   # Resultado: <class 'str'>
print(type(idade))  # Resultado: <class 'int'>
print(type(altura)) # Resultado: <class 'float'>
print(type(esta_estudando)) # Resultado: <class 'bool'>

# 3. OPERAÇÕES BÁSICAS
# -----------------

# Operações matemáticas
a = 10
b = 3

soma = a + b        # Adição
subtracao = a - b   # Subtração
multiplicacao = a * b  # Multiplicação
divisao = a / b     # Divisão (resultado é float)
divisao_inteira = a // b  # Divisão inteira (resultado é int)
resto = a % b       # Resto da divisão
potencia = a ** b   # Potenciação (a elevado a b)

print(f"Soma: {soma}")             # Resultado: Soma: 13
print(f"Subtração: {subtracao}")   # Resultado: Subtração: 7
print(f"Multiplicação: {multiplicacao}")  # Resultado: Multiplicação: 30
print(f"Divisão: {divisao}")       # Resultado: Divisão: 3.3333333333333335
print(f"Divisão inteira: {divisao_inteira}")  # Resultado: Divisão inteira: 3
print(f"Resto: {resto}")           # Resultado: Resto: 1
print(f"Potência: {potencia}")     # Resultado: Potência: 1000

# 4. STRINGS (TEXTOS)
# ---------------

# Operações com strings
primeiro_nome = "João"
sobrenome = "Silva"

# Concatenação (juntar strings)
nome_completo = primeiro_nome + " " + sobrenome
print(nome_completo)  # Resultado: João Silva

# Repetição
print("="*20)  # Resultado: ====================

# Métodos de strings
texto = "python é incrível"
print(texto.upper())     # Resultado: PYTHON É INCRÍVEL
print(texto.capitalize())  # Resultado: Python é incrível
print(texto.find("é"))   # Resultado: 7 (posição do caractere)
print(texto.replace("incrível", "fantástico"))  # Resultado: python é fantástico

# 5. ENTRADA DE DADOS
# ----------------

# Recebendo dados do usuário
# nome_usuario = input("Digite seu nome: ")
# idade_usuario = int(input("Digite sua idade: "))
# Comentamos estas linhas para evitar que o código pare esperando entrada

# Exemplo de como seria o uso:
nome_usuario = "Carlos"  # Simulando a entrada do usuário
idade_usuario = 30       # Simulando a entrada do usuário

print(f"Olá {nome_usuario}, você tem {idade_usuario} anos!")
# Resultado: Olá Carlos, você tem 30 anos!

# 6. ESTRUTURAS CONDICIONAIS
# ----------------------

# if, elif, else
idade = 18

if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Acabou de atingir a maioridade")  # Este será o resultado
else:
    print("Maior de idade")

# Operadores de comparação
# == (igual a), != (diferente de), > (maior que), < (menor que)
# >= (maior ou igual a), <= (menor ou igual a)

# Operadores lógicos
tem_carteira = True
tem_idade = idade >= 18

if tem_idade and tem_carteira:
    print("Pode dirigir")  # Este será o resultado
else:
    print("Não pode dirigir")

# 7. ESTRUTURAS DE REPETIÇÃO
# -----------------------

# Loop for
print("Contando de 1 a 5:")
for i in range(1, 6):  # range(inicio, fim) - o fim não é incluído
    print(i)
# Resultado:
# Contando de 1 a 5:
# 1
# 2
# 3
# 4
# 5

# Loop while
print("Contagem regressiva:")
contador = 3
while contador > 0:
    print(contador)
    contador -= 1  # Equivalente a: contador = contador - 1
# Resultado:
# Contagem regressiva:
# 3
# 2
# 1

# 8. LISTAS
# -------

# Criando listas
frutas = ["maçã", "banana", "laranja", "uva"]
numeros = [1, 2, 3, 4, 5]

# Acessando elementos
print(frutas[0])  # Resultado: maçã (o primeiro elemento tem índice 0)
print(frutas[-1])  # Resultado: uva (índice negativo conta do final para o início)

# Modificando elementos
frutas[1] = "morango"
print(frutas)  # Resultado: ['maçã', 'morango', 'laranja', 'uva']

# Adicionando elementos
frutas.append("abacaxi")  # Adiciona ao final da lista
print(frutas)  # Resultado: ['maçã', 'morango', 'laranja', 'uva', 'abacaxi']

# Removendo elementos
frutas.remove("laranja")  # Remove pelo valor
print(frutas)  # Resultado: ['maçã', 'morango', 'uva', 'abacaxi']

ultimo_item = frutas.pop()  # Remove e retorna o último item
print(ultimo_item)  # Resultado: abacaxi
print(frutas)  # Resultado: ['maçã', 'morango', 'uva']

# 9. FUNÇÕES
# --------

# Definindo uma função simples
def saudacao(nome):
    return f"Olá, {nome}!"

# Chamando a função
mensagem = saudacao("Ana")
print(mensagem)  # Resultado: Olá, Ana!

# Função com parâmetros padrão
def calcular_potencia(base, expoente=2):
    return base ** expoente

print(calcular_potencia(3))     # Resultado: 9 (3^2)
print(calcular_potencia(2, 3))  # Resultado: 8 (2^3)

# 10. DICIONÁRIOS
# ------------

# Criando um dicionário (estrutura chave-valor)
pessoa = {
    "nome": "Pedro",
    "idade": 28,
    "profissao": "Desenvolvedor"
}

# Acessando valores
print(pessoa["nome"])  # Resultado: Pedro

# Adicionando novos pares chave-valor
pessoa["cidade"] = "São Paulo"
print(pessoa)  # Resultado: {'nome': 'Pedro', 'idade': 28, 'profissao': 'Desenvolvedor', 'cidade': 'São Paulo'}

# Verificando se uma chave existe
if "profissao" in pessoa:
    print(f"Profissão: {pessoa['profissao']}")  # Resultado: Profissão: Desenvolvedor