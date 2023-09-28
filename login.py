users = []
senhas = []
login = input('Digite o seu login para cadastro: ')
users.append(login)
senha = input('Digite a sua senha para cadastro: ')
senhas.append(senha)

if login in users:
    if senha in senha:
        print('Logado com sucesso.')
    else:
        print('Usuário ou senha incorreto.')

