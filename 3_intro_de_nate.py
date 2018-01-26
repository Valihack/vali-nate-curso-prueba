

#Funcion type te devuelve el tipo de variable
a=type(1)
print(a)
a=type(1.2)
print(a)
a=type(True)
print(a)
a=type("Hola")
print(a)
a=str(a)
if a == "class 'str'":
    print("hola si va asi")

#Hacer strings
edad=12
ano=1999

print("Tengo {} años y naci en {}".format(edad, ano))