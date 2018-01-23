def mayor(lista):
    numero=0
    i=0
    while i < len(lista):
        if lista[i]>numero:
            numero=lista[i]
        i+=1
    return numero

n_1=int(input("Introduce un número 1: "))
n_2=int(input("Introduce un número 2: "))
n_3=int(input("Introduce un número 3: "))
lista=[n_1,n_2,n_3]

print(mayor(lista))



