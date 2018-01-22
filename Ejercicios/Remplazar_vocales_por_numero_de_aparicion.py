texto=input("Introduce un texto: ")

numero=1
contador=0
nuevo_texto=""

while len(texto)>contador:
    if texto[contador] == "a" or texto[contador] == "e" or texto[contador] == "i" or texto[contador] == "o" or texto[contador] == "u":
        nuevo_texto+=str(numero)
        numero+=1
    else:
        nuevo_texto+=texto[contador]
    contador+=1
print(nuevo_texto)
