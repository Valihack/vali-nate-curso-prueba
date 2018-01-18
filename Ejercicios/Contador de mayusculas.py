import string
alfabeto_de_mayusculas=list(string.ascii_uppercase)
contador_mayusculas=0
texto=input("Introduce el texto: ")

for caracter in texto:
    if caracter in alfabeto_de_mayusculas:
        contador_mayusculas+=1


print("Este texto tiene {} mayusculas".format(contador_mayusculas))