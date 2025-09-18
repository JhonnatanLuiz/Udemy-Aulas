# Operador lógico "or": Retorna True se pelo menos uma das condições for verdadeira.  

"""entrada = input('[E]ntrar ou [S]air? ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')"""

#Avaliação de curto-circuito com o operador "or":
# Se a primeira condição (entrada == 'E' or entrada == 'e') for verdadeira, a segunda condição (senha_digitada == senha_permitida) não será avaliada.
# Isso é útil para evitar erros, como tentar acessar uma variável que não existe ou executar uma operação que não faz sentido.
# Exemplo de uso do operador "or":

senha = input('Digite a senha: ') or 'Sem senha'
print(senha) # Output: Se o usuário não digitar nada, 'Sem senha' será atribuído à variável senha.
# Se o usuário digitar algo, esse valor será atribuído à variável senha.
