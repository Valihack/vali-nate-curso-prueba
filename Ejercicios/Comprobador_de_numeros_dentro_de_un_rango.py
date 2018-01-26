def rango(principio, numero, fin):
    if principio>fin:
        aux=principio
        principio=fin
        fin=aux
    if numero>fin or numero<principio:
        return False
    else:
        return True

principio=int(input("Introduce un principio: "))
fin=int(input("Introduce un fin: "))
numero=int(input("Introduce un número a comprobar: "))


print(rango(principio, numero, fin))

