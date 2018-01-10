print('1 Para sumar, restar, multiplicar y dividir'
      '2 Para elevar a una potencia'
      '3 Para calcular el resto')

c=int(input("Elige: "))

print(5/2)


if c == 1 :
    a = int(input("Introduce un numero a"))
    b = int(input("Introduce un numero b"))
    print(a+b)
    print(a - b)
    print(a * b)
    print(a / b)

if c == 2 :
    a = int(input("Introduce un numero a: "))
    d=int(input("Dime la potencia a la que deseas elevar: "))
    count = 1
    while (count<d):
        a=a*a
        count=count+1
    print(a)

if c == 3 :
    a = int(input("Introduce un numero a: "))
    b = int(input("Introduce un numero b: "))
    d = a % b
    print(d)