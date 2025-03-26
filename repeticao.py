def envia_email(cliente):
    print(f'Email enviado para o cliente {cliente}!')

clientes = ['Ana', 'Jonas', 'Felipe', 'Gabriel', 'Renato']

for cliente in clientes:
    envia_email(cliente)

for i, cliente in enumerate(clientes):
    print(i, cliente)

###########################################################
numero = 0

while numero < 5:
    print(numero)
    numero += 1

numero = 0

while numero < 5:
    if numero == 2:
        break
   
    print(numero)
    numero += 1

for i in range(10):
    print(i)
###########################################################
def envia_email(cliente):
    print(f'Email enviado para o cliente {cliente}!')

clientes = ['Ana', 'Jonas', 'Felipe', 'Gabriel', 'Renato']

for i, cliente in enumerate(clientes):
    envia_email(cliente)
    
    if i == 2:
        break


for i, cliente in enumerate(clientes):
    if i == 2:
        break

    envia_email(cliente)

for i, cliente in enumerate(clientes):
    if i == 2:
        continue

    envia_email(cliente)


    