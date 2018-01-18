cantidad_numeros=int(input("Cuantos numero quieres introducir: "))

numeros_usuario=[]
numero_del_usuario=""
while len(numeros_usuario)<cantidad_numeros:
    while not numero_del_usuario.isdigit():
        numero_del_usuario=input("Introduce numero: ")
    numeros_usuario.append(numero_del_usuario)
    numero_del_usuario=""
    print("Añadido!")

numero_pequeno=numeros_usuario[0]

for numero in numeros_usuario:
    if numero < numero_pequeno:
        numero_pequeno=numero
print("El numero mas pequeño es el {}".format(numero_pequeno))