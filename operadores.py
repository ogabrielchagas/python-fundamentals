a = True
b = False

if a and b:
    print('Atendeu a condição')
else:
    print('Não atendeu a condição')

if a or b:
    print('Atendeu a condição')
else:
    print('Não atendeu a condição')
############################################################

idade = 25
nome = 'Gabriel'
peso = 90

if idade == 25:
    print('Idade correta')
else:
    print('Idade incorreta')

if idade != 25:
    print('Idade correta')
else:
    print('Idade incorreta')

if nome == 'Gabriel' and idade == 24:
    print("Dados corretos")
else:
    print("Dados incorretos")

if nome == 'Gabriel' or idade == 24:
    print("Dados corretos")
else:
    print("Dados incorretos")

if (nome == 'Gabriel' or idade == 24) and peso == 90:
    print("Dados corretos")
else:
    print("Dados incorretos")