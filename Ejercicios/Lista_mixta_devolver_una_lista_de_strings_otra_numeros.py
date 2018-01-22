cantidad_elementos=int(input("Cuantos numero quieres introducir: "))
lista_usuario=[]
numeros_usuario=[]
strings_usuario=[]
numero_del_usuario=""
while len(lista_usuario)<cantidad_elementos:
    elemento_usuario=input("Introduce: ")
    lista_usuario.append(elemento_usuario)
    print("Añadido!")

contador=0

while len(lista_usuario)>contador:
    elemento_usuario=lista_usuario[contador]
    if elemento_usuario.isdigit():
        numeros_usuario.append(elemento_usuario)
    else:
        strings_usuario.append(elemento_usuario)
    contador+=1

print(numeros_usuario)
print(strings_usuario)