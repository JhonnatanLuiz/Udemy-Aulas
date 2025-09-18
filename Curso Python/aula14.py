#função format() formata uma string, permitindo a inclusão de variáveis dentro dela.
# A função format() é usada para formatar strings, permitindo a inclusão de variáveis dentro delas.
a = 'A'
b = 'B'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c) #parametro nomeado é o mesmo que o parametro posicional, mas com nome.

print(formato)