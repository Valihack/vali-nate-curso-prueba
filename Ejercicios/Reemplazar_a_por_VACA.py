texto=input("Introduce un texto: ")
contador=0

valor_sustituir=["VACA"]

for valor in valor_sustituir:
    texto=texto.replace("A", valor)
    texto=texto.replace("a", valor)


print(texto)