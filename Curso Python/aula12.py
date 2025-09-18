nome = 'Jhonnatan Luiz'
altura = 1.75
peso = 80
imc = peso / (altura ** 2) # Índice de Massa Corporal (IMC)
print('Nome:', nome) # Resultado: Nome: Jhonnatan Luiz
print('Altura:', altura) # Resultado: Altura: 1.75
print('Peso:', peso) # Resultado: Peso: 80
print('IMC:', imc) # Resultado: IMC: 26.122448979591837

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso normal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 35:
    print('Obesidade grau 1')
elif imc >= 35 and imc < 40:
    print('Obesidade grau 2')
else:
    print('Obesidade grau 3')

