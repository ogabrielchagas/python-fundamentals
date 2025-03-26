lista = [] #Como declarar lista vazia em python
print(lista)

carros = []
carros.append('Marea')  #Uma das formas de adicionar elementos na lista
carros.append('Fusca')  #Listas em Python podem ter diferentes tipos de variáveis em seus elementos
carros.append(10)
print(carros)
####################################################################################

carros = ['Marea', 'Fusca', 'Chevette']
carros.append('Corcel') #append sempre adiciona o novo elemento ao final da lista
print(carros)
print(carros[2])

carros.insert(1, 'Escort')  #insert insere o elemento na posição especificada na função
print(carros)

carros.pop()    #pop remove o último elemento da lista
print(carros)

del carros[1]   #del remove um elemento pelo índice
print(carros)

carros.remove('Chevette') #remove um elemento baseado no seu valor, lembrando que o valor deve ser identico ao da lista
print(carros)

print(carros.count('Fusca'))    #Conta quantas vezes o elemento especificado aparece na lista
carros.append('Fusca')
print(carros.count('Fusca'))
carros.pop() 

carros.append('Kombi') 
print(carros)

carros.reverse()    #Reverte a ordem dos elementos de uma lista
print(carros)

carros.sort()   #Organiza a lista em ordem alfanúmerica crescente (alfábetica ou de números do menor ao maior)
print(carros)

numeros = [5,12,3,1]
print(numeros)
numeros.sort()
print(numeros)