#\r\n -> CRLF (Carriage Return + Line Feed)
#\n -> LF (Line Feed)
print(12,34, 1011, sep="-", end='##\n') #argumento não nomeado
print(12,34, sep='-', end='\n') # Sep significa separador, o padrão é espaço
print(12,34, sep='-', end='\n') # Resultado: 12-34