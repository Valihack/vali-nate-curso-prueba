
numero_a_adivinar=int(input("Usuario 1 introduzca el numero a adivinar: "))

contador = 0

while contador < 5:
    intento=int(input("Usuario 2 introduce un numero: "))
    if intento==numero_a_adivinar:
        print("Has adivinado el numero felicidades!!!")
        break
    else:
        print("Vuelve a intentarlo")
        contador+=1