from time import sleep
import random

def write_file_and_screen(text, file_name):
    with open(file_name, "a") as hours_file:
        hours_file.write(text)
        print(text)
def main():

    TIME = 3
    while True:
        lista_de_strings = ("C'est la vie\n","Don't be mad bro\n","Just chill it\n", "PIng POng Theory\n")
        max_item=int(len(lista_de_strings)-1)
        write_file_and_screen(lista_de_strings[int(random.randint(0,max_item))], "Frases aleatorias.txt")
        sleep(TIME)

if __name__ == "__main__":
    main()