import string

texto = 'AULA PYCODEBR'

print(texto[0]) #texto[4], texto[5], texto[-1] = R
print(texto[5:11]) #PYCODE -> 5:11 com 11 excluso pega os caracteres do 5 ao 10
print(texto[0:4]) #AULA
print(texto[5:]) #PYCODEBR -> Pega a partir do caracter 5 e até o final da string
print(texto[:4]) #AULA -> Pega do primeiro caracter até o 4 caracter excluindo o 4

print(len(texto)) #retorna o tamanho da string
print(texto.count('A')) #Conta e retorna a quantidade do caracters especificado
print(texto.count('A', 5, 11)) #Retorna a quantidade do caracter especificado dentro do range estabelecido (5-11)
print(texto.count('AULA')) #Também consegue contar e buscar palavras

print(texto.find('AULA')) #Retorna a posição em que a letra ou palavra especificada começa, no caso posição 0
print(texto.find('PYCODEBR')) #Aqui ele encontra a partir do caracter 5

print(texto.upper()) #Retorna toda a string em letras maiusculas
print(texto.lower()) #Retorna toda a string em letras minusculas

print(texto.capitalize()) #Retorna a primeira letra da string em maiuscula e o resto minusculo
print(texto.title()) #Retorna a primeira letra de cada palavra da string em maiuscula e o resto minusculo

print(texto.split()) #Retorna uma lista com todas as palavras da sua string, divide no espaço entre as palavras

lista_palavras = texto.split()  
lista_palavras = ''.join(lista_palavras) #Junta uma lista em uma frase, com esta ''.join ele não dá espaços
print(lista_palavras)

lista_palavras = texto.split()
print(' '.join(lista_palavras)) #Nesse caso demos um espaço ao usar ' '.join, esse valor (' ') pode ser qualquer

texto = '   AULA PYCODEBR   '
print(texto.strip()) #Funciona como um trim, ele está retirando os espaços em branco

texto = '   AULA PYCODEBR   '
print(texto.rstrip()) #Remove os espaços apenas na direita da string

texto = '   AULA PYCODEBR   '
print(texto.lstrip()) #Remove os espaços apenas na esquerda da string