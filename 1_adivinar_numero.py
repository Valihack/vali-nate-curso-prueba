import random


a=0


while (5 > a):

    random_number = random.randrange(10)
    numero_del_usuario = int(input("Dime un numero: "))

    if numero_del_usuario == random_number:
        print("Has acertado el {} es el correcto".format(numero_del_usuario))
    if not numero_del_usuario == random_number:
        print("No has acertado")
    a+=1