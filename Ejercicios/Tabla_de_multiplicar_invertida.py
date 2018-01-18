multiplo=int(input("Introduce la tabla de multiplicar que quieres ver: "))

multiplicador=10

while multiplicador > 0:
    print("{} x {} = {}".format(multiplo, multiplicador, multiplo*multiplicador))
    multiplicador-=1