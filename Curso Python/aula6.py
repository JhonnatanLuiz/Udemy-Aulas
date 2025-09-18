# conversão de tipos, coerção de tipos, conversão implícita e explícita, coerção implícita e explícita
# type convertion, typecasting, coercion, implicit conversion, explicit conversion
# é o ato de converter um valor de um tipo de dado para outro tipo de dado.
# Isso pode ser feito de forma implícita (automática) ou explícita (manual).
# tipos imutáveis: str, int, float, bool, tuple, frozenset, bytes
# tipos mutáveis: list, set, dict, bytearray, memoryview
# tipos primitivos: int, float, bool, str, bytes
print(int('1'), type(int('1'))) #Resultado: 1 <class 'int'> (inteiro)
print(float('1') + 1) #Resultado: 2.0 (float)
print(type(float('1') + 1)) #Resultado: <class 'float'> (float)
print(bool('')) #Resultado: False (string vazia é considerada False)
print(str(11) + 'b') #Resultado: 11b (string)