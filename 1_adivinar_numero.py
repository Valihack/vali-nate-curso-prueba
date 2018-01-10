import random
while (1 > 0):

    random_number = random.randrange(10)
    numero_del_usuario = int(input("Dime un numero: "))

    if numero_del_usuario == random_number:
        print("Has acertado el "+ str(numero_del_usuario) + " es el correcto")
    if not numero_del_usuario == random_number:
        print("No has acertado")