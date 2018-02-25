import random
from time import sleep



def main():
    TIEMPO=3
    while True:
        cuenta_atras = TIEMPO
        for i in range(0,TIEMPO):
            print(str(cuenta_atras) + "...")
            sleep(1)
            cuenta_atras-=1

        print("Adivina el numero que se ha calculado")
        if int(input("Introduce el numero del 1 al 10: ")) == 3:
            print("MUY BIEN LO HAS ADIVINADO!!!")
        else:
            print("Prueba otra vez se esta recalculando")









if __name__ == "__main__":
    main()