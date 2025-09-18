# Tipos int e float são usados para representar números inteiros e de ponto flutuante, respectivamente.
# int: Números inteiros, como 1, 2, 3, -1, -2, -3.
# O tipo int representa números inteiros, ou seja, números sem parte decimal.
# positivo ou negativo. Int sem sinal é considerado positivo.
print(11) #inteiro positivo
print(-11) #inteiro negativo
print(0) #inteiro zero

#float: Números de ponto flutuante, como 1.0, 2.5, -3.14.
print(11.0) #float positivo
print(-11.0) #float negativo

# A função type() retorna o tipo de dado de uma variável.
print( type('11.0') ) #Resultado: <class 'str'> (string)
print( type(0) ) #Resultado: <class 'int'> (inteiro)
print( type(1.1)), type(-1.1), type(0.0) #Resultado: <class 'float'> (float)
