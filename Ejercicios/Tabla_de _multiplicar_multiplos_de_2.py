multiplo=int(input("Introduce la tabla de multiplicar que quieres ver: "))

multiplicador=2

while multiplicador < 11:
    print("{} x {} = {}".format(multiplo, multiplicador, multiplo*multiplicador))
    multiplicador+=2