texto=input("Introduce el texto: ")
n_espacio=0
n_punto=0
n_coma=0
espacio=[" "]
punto=["."]
coma=[","]

for caracter in texto:
    if caracter in espacio:
       n_espacio += 1
    elif caracter in punto:
        n_punto+=1
    elif caracter in coma:
        n_coma+=1

print("Hay {} espacios, {} puntos y {} coomas".format(n_espacio,n_punto,n_coma))