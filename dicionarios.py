#Em dicionarios, diferente das listas, nos temos uma estrutura que possui chave e valor, podendo organizar os seus
#dados de forma muito fácil e rapida

lista = ['Um', 'Dois', 'Três']
print(lista[0])

meu_dicio = {}  #Esta é a forma de inicializar um dicionario vazio
print(meu_dicio)

meu_dicio = {
    'nome': 'Gabriel',
    'idade': 24,
    'profissao': 'Dev'
}

print(meu_dicio)
print(meu_dicio['nome'])
print(meu_dicio['profissao'])

print(meu_dicio.get('idade'))
meu_dicio.pop('idade')  #Diferente do pop de listas aqui deve-se passar o nome da chave a ser removida
print(meu_dicio)

print(meu_dicio.keys()) #Mostra somente as chaves do dict
print(meu_dicio.values())   #Mostra somente os valores do dict

meu_dicio.clear()
print(meu_dicio)
###################################################################################################

pessoa = {
    'nome': 'Gabriel',
    'idade': 24,
    'profissao': 'Dev',
    'interesses': ['Python', 'Programação', 'Automobilismo'],
    'pet': {
        'nome': 'Loki',
        'idade': 5,
        'peso': '35kg'
    }
}

print(pessoa)
print(pessoa.get('nome'))
print(pessoa.get('interesses'))
print(pessoa.get('interesses')[0])
print(pessoa['interesses'][1])

print(pessoa.get('pet'))
print(pessoa.get('pet').get('nome'))

print(pessoa['pet']['idade'])

pessoa = {
    'nome': 'Gabriel',
    'idade': 24,
    'profissao': 'Dev',
    'interesses': ['Python', 'Programação', 'Automobilismo'],
    'pet': {
        'nome': 'Loki',
        'idade': 5,
        'peso': '35kg'
    }
}

pessoa['ano_nascimento'] = 2000
pessoa['cores_fav'] = ['Verde', 'Vermelho', 'Preto']
pessoa['mãe'] = {
    'nome': 'Adriana',
    'idade': 50,
}

print(pessoa)