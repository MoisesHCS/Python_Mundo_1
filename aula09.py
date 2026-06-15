frase = "Curso em Vídeo Python"
frase2 = "   Aprenda Python  "
print(frase[9::3]) #Seleciona o começo, o fim e de quanto em quanto pula
print(len(frase)) #Comprimento da frase
print(frase.count("o")) #Conta quantos caracteres tem
print(frase.count("o", 0, 13)) #Conta quantos caracteres tem partindo de um começo e um fim
print(frase.find("deo")) #Encontra a primeira posição dessa frase
print(frase.find("Android")) #Se nao houver essa palavra ou frase, retorna -1
print('Curso' in frase) #Retorna True ou False, verifica se há a palavra na frase
#frase.replace("Python", "Android") #Troca uma palavra por outra na frase
print(frase.upper()) #Deixa todas as letras em maísculo
print(frase.lower()) #Deixa todas as letras em minúsculo
print(frase.capitalize()) #Deixa apenas a primeira letra da frase em maísculo
print(frase.title()) #Deixa a primeira letra de todas as palavras em maísculo
print(frase2.strip()) #Remove os espaços do começo e do fim da string
print(frase2.rstrip()) #Remove apenas os espaços do fim (direita)
print(frase2.lstrip()) #Remove apenas os espaços do começo (esquerda)
print(frase.split()) #Considera os espaços e gera uma lista com cada palavra, e cada palavra terá um índice
lista = frase.split() #Gerando a lista
print("-".join(lista)) #Juntando a lista, colocando "-" no lugar dos espaços