#Funcoes nativas
len('teste')

meu_dicio = dict()  

#Funcoes personalizadas

def minha_funcao():
    print('teste')

minha_funcao()

def somar(a, b):
    res = a + b
    return res

print(somar(2, 4))


def envia_email():
    email = 'exemplo@gmail.com'
    senha = '12345'
    email_envio = "outro@gmail.com"
    #conecta no provedor de email
    #monta corpo do email
    #envia email
    return 'Email enviado!'

pessoas = ['Felipe', 'Gabriel', 'Mariana']

for pessoa in pessoas:
    print(envia_email())
    #email_enviado =  envia_email()
    #print(email_enviado)
###################################################################################3

def envia_email_outro(nome_destinario, email_destinario):
    email = 'teste@gmail.com'
    senha = '12345'

    nome_dest = nome_destinario
    email_dest = email_destinario

    #conecta no provedor de email
    #monta corpo do email
    #envia email

    return f'Email enviado para {nome_dest}, dono(a) do email {email_dest}'

pessoas = [
    {
        'nome': 'Felipe',
        'email': 'felipe@gmail.com'
    },
    {
        'nome': 'Gabriel',
        'email': 'gabriel@gmail.com'
    },
    {
        'nome': 'Mariana',
        'email': 'mariana@gmail.com'
    }
]

for pessoa in pessoas:
    print(envia_email_outro(pessoa['nome'], pessoa['email']))
    #email_enviado =  envia_email()
    #print(email_enviado)