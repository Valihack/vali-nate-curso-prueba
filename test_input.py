import random
while (1 > 0):

    random = random.randrange(10)
    numero_del_usuario = int(input("Dime un numero: "))

    if numero_del_usuario == random:
        print("Has acertado el "+ str(numero_del_usuario) + " es el correcto")
    if not numero_del_usuario == random:
        print("No has acertado")