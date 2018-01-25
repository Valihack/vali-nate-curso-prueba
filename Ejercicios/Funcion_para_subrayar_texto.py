texto=input("Introduce el texto: ")

def mostrar_titulo_subrayado (texto):
    n_caracteres=len(texto)
    i=0
    subrayado=""
    while i < n_caracteres:
        subrayado+="_"
        i+=1
    return subrayado

print(texto)
print(mostrar_titulo_subrayado(texto))