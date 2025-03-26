def login(usuario, senha):
    if usuario == 'chagas' and senha == '0420':
        return 'Login correto, você está logado!'
    else:
        return 'Login incorreto, você foi desconectado!'