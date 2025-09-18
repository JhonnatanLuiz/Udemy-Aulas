import random

def gerar_cpf():
    # Gera os 9 primeiros dígitos aleatórios
    nove_digitos = ''.join(str(random.randint(0, 9)) for _ in range(9))

    # Calcula o primeiro dígito verificador
    soma = 0
    regressivo = 10
    for digito in nove_digitos:
        soma += int(digito) * regressivo
        regressivo -= 1
    digito_1 = (soma * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    # Calcula o segundo dígito verificador
    dez_digitos = nove_digitos + str(digito_1)
    soma2 = 0
    regressivo2 = 11
    for digito in dez_digitos:
        soma2 += int(digito) * regressivo2
        regressivo2 -= 1
    digito_2 = (soma2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'
    return cpf_gerado

if __name__ == "__main__":
    quantidade = int(input('Quantos CPFs deseja gerar? '))
    for _ in range(quantidade):
        cpf = gerar_cpf()
        print(f'CPF gerado: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}')
