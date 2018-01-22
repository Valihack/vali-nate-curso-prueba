cantidad_numeros=int(input("Introduce cuantos numeros quieres introducir: "))

numeros_usuario=[]
numero_del_usuario=""

while len(numeros_usuario)<cantidad_numeros:
    numero_del_usuario=int(input("Introduce numero: "))
    numeros_usuario.append(numero_del_usuario)
    print("Añadido!")
palabra=""
for contador in range(len(numeros_usuario)):
    if numeros_usuario[contador] % 3 == 0:
        palabra+="Fizz"
    if numeros_usuario[contador] % 5 == 0:
        palabra+="Buzz"
    if palabra == "FizzBuzz":
        palabra="Bazinga"
    if not palabra == "":
        numeros_usuario[contador]=palabra
        palabra = ""
print(numeros_usuario)