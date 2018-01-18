texto=input("Introduce un texto: ")

vocales=["a","e","i","o","u"]
lista_vocales=[]
for caracter in texto:
    if caracter in vocales:
        lista_vocales.append(caracter)

print(lista_vocales)