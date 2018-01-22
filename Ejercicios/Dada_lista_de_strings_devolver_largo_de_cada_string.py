numero_strings=int(input("Cuantas strings quieres introducir: "))

strings_usuario=[]
string=""
while len(strings_usuario)<numero_strings:
    string=input("Introduce numero: ")
    strings_usuario.append(string)
    string=""
    print("Añadido!")

contador=0
numero_caracteres=0

while len(strings_usuario)>contador:
    numero_caracteres=len(strings_usuario[contador])
    print("El elemento {}, {}, tiene {} caracteres".format(contador+1,strings_usuario[contador],numero_caracteres))
    numero_caracteres=0
    contador+=1