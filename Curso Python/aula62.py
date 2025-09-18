"""
Exercício

Calculo do primeiro e segundo dígito do CPF
CPF: 746.824.890-70
"""

cpf = "746824890"  # Os 9 primeiros dígitos do CPF
multiplicadores = list(range(10, 1, -1))  # Contagem regressiva de 10 a 2

# Calcular soma dos produtos para o primeiro dígito
soma = sum(int(cpf[i]) * multiplicadores[i] for i in range(9))
resultado = (soma * 10) % 11
primeiro_digito = 0 if resultado > 9 else resultado

# Cálculo do segundo dígito do CPF
cpf_com_primeiro = cpf + str(primeiro_digito)
multiplicadores2 = list(range(11, 1, -1))  # Contagem regressiva de 11 a 2
soma2 = sum(int(cpf_com_primeiro[i]) * multiplicadores2[i] for i in range(10))
resultado2 = (soma2 * 10) % 11
segundo_digito = 0 if resultado2 > 9 else resultado2

print(f"O primeiro dígito do CPF é {primeiro_digito}")
print(f"O segundo dígito do CPF é {segundo_digito}")
