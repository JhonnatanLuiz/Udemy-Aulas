"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
# Importa os módulos necessários
import re
import sys

# Recebe o CPF do usuário e remove caracteres não numéricos
entrada = input('CPF [746.824.890-70]: ')
cpf_enviado_usuario = re.sub(
    r'[^0-9]',
    '',
    entrada
)

# Verifica se o CPF enviado é uma sequência repetida (ex: 11111111111)
entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

# Pega os 9 primeiros dígitos do CPF
nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10

# Calcula o primeiro dígito verificador
resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
# Aplica as regras para obter o primeiro dígito
# Multiplica a soma por 10, pega o resto da divisão por 11
# Se o resultado for maior que 9, o dígito é 0, senão é o próprio resultado
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

# Adiciona o primeiro dígito ao final dos 9 dígitos para calcular o segundo dígito
# e reinicia o contador regressivo
dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

# Calcula o segundo dígito verificador
resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
# Aplica as regras para obter o segundo dígito
# Multiplica a soma por 10, pega o resto da divisão por 11
# Se o resultado for maior que 9, o dígito é 0, senão é o próprio resultado
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

# Monta o CPF gerado pelo cálculo (9 dígitos + 2 dígitos verificadores)
cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

# Compara o CPF enviado pelo usuário com o CPF gerado pelo cálculo
# Mostra o número do CPF e se é válido ou inválido
if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'CPF {cpf_enviado_usuario} é válido')
else:
    print(f'CPF {cpf_enviado_usuario} é inválido')