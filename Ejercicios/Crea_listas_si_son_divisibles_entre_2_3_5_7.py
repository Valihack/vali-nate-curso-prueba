cantidad_numeros=int(input("Cuantos numero quieres introducir: "))
numeros_usuario=[]
numero_del_usuario=""

while len(numeros_usuario)<cantidad_numeros:
    numero_del_usuario=int(input("Introduce numero: "))
    numeros_usuario.append(numero_del_usuario)
    print("Añadido!")

multiplos_de_dos=[]
multiplos_de_tres=[]
multiplos_de_cinco=[]
multiplos_de_siete=[]

for contador in range(len(numeros_usuario)):

    if numeros_usuario[contador] % 2 == 0:
        multiplos_de_dos.append(numeros_usuario[contador])
    if numeros_usuario[contador] % 3 == 0:
        multiplos_de_tres.append(numeros_usuario[contador])
    if numeros_usuario[contador] % 5 == 0:
        multiplos_de_cinco.append(numeros_usuario[contador])
    if numeros_usuario[contador] % 7 == 0:
        multiplos_de_siete.append(numeros_usuario[contador])

print(multiplos_de_dos,multiplos_de_tres,multiplos_de_cinco,multiplos_de_siete)