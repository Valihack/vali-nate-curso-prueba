
multiplo=int(input("Introduce la tabla de multiplicar que quieres ver: "))

multiplicador=5

while multiplicador < 16:
    print("{} x {} = {}".format(multiplo, multiplicador, multiplo*multiplicador))
    multiplicador+=1