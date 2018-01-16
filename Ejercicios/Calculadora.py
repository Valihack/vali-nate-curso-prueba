print("1) Sumar")
print("2) Restar")
print("3) Multiplicar")
print("4) Dividir")

seleccion=int(input())

primer_numero=int(input("Primer numero: "))
segundo_numero=int(input("Segundo numero: "))

if seleccion==1:
    print(primer_numero + segundo_numero)

elif seleccion==2:
    print(primer_numero - segundo_numero)

elif seleccion==3:
    print(primer_numero * segundo_numero)

elif seleccion == 4:
    print(primer_numero / segundo_numero)


