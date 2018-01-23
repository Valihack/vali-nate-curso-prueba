def rango(principio, numero, fin):
    if principio>fin:
        aux=principio
        principio=fin
        fin=aux
    if numero>fin or numero<principio:
        return False
    else:
        return True

principio=int(input("Introduce un número 1: "))
fin=int(input("Introduce un número 2: "))
numero=int(input("Introduce un número 3: "))


print(rango(principio, numero, fin))

