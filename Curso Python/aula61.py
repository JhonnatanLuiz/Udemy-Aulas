"""
Exercício

Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

'''cpf = '746824890'  # 9 primeiros dígitos do CPF
soma = 0
regressivo = 10

for digito in cpf:
    soma += int(digito) * regressivo
    regressivo -= 1

resultado = (soma * 10) % 11
primeiro_digito = resultado if resultado <= 9 else 0

print(f'O primeiro dígito do CPF é {primeiro_digito}')'''

cpf = "746824890"  # Os 9 primeiros dígitos do CPF
multiplicadores = list(range(10, 1, -1))  # Contagem regressiva de 10 a 2

# Calcular soma dos produtos
soma = sum(int(cpf[i]) * multiplicadores[i] for i in range(9))

# Multiplicar por 10 e obter o resto da divisão por 11
resultado = (soma * 10) % 11

# Aplicar regra final: se o resultado for maior que 9, considerar 0
primeiro_digito = 0 if resultado > 9 else resultado

print(f"O primeiro dígito do CPF é {primeiro_digito}")

# Cálculo do segundo dígito do CPF
cpf_com_primeiro = cpf + str(primeiro_digito)
multiplicadores2 = list(range(11, 1, -1))  # Contagem regressiva de 11 a 2

# Calcular soma dos produtos para o segundo dígito
soma2 = sum(int(cpf_com_primeiro[i]) * multiplicadores2[i] for i in range(10))

# Multiplicar por 10 e obter o resto da divisão por 11
resultado2 = (soma2 * 10) % 11

# Aplicar regra final: se o resultado for maior que 9, considerar 0
segundo_digito = 0 if resultado2 > 9 else resultado2

print(f"O segundo dígito do CPF é {segundo_digito}")
