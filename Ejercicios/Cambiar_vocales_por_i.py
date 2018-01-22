texto=input("Introduce un texto: ")
contador=0

valor_sustituir=["i"]

for valor in valor_sustituir:
    texto=texto.replace("a", valor)
    texto=texto.replace("e", valor)
    texto = texto.replace("o", valor)
    texto = texto.replace("u", valor)


print(texto)