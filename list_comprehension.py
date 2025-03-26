numeros = [1,2,3,4,5]   

dobro = []

for numero in numeros:
    dobro.append(numero * 2)

print(dobro)

numeros_dobrados = [numero * 2 for numero in numeros] 
print(numeros_dobrados)

def triplo(num):
    return num * 3

triplo = [triplo(numero) for numero in numeros]
print(triplo)
##############################################################3

nomes = ['Ana', 'Gabriel', 'Mariana', 'João', 'Carlos']

maiusculas = [nome.upper() for nome in nomes]
print(maiusculas)

apenas_a = [nome.upper() for nome in nomes if nome.count('a') >= 1]
print(apenas_a)