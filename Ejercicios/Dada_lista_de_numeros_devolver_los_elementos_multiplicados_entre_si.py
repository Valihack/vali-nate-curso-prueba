cantidad_numeros=int(input("Cuantos numero quieres introducir: "))

numeros_usuario=[]
numero_del_usuario=""
while len(numeros_usuario)<cantidad_numeros:
    while not numero_del_usuario.isdigit():
        numero_del_usuario=input("Introduce numero: ")
    numeros_usuario.append(numero_del_usuario)
    numero_del_usuario=""
    print("Añadido!")


numero_elementos=len(numeros_usuario)
contador=0
resultado=1

while numero_elementos>contador:
    resultado=int(numeros_usuario[contador])*resultado
    contador+=1

print("El resulta de la multiplicacion de todos los elemetos de la lista es: {}".format(resultado))
