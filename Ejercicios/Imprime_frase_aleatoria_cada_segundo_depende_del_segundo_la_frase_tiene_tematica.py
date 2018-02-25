from time import sleep
import random

def main():
    full_list = [['Hoy va a ser un buen dia\n', 'Hoy me voy a comer el mundo\n', 'No hay dos sin tres\n', 'Dora, Dora, Dora, exploradoraaaa'],['silla\n', 'mesa\n', 'comoda\n', 'aramrio\n', 'butaca\n', 'sofa\n'],['cocacola\n', 'agua\n', 'vino\n', 'fanta\n', 'mixta\n', 'whisky\n'],['chupamela\n', 'joputa\n', 'si espanya fos un donuts madrid no existiria\n', 'luis enrique tu apdre es amunique\n', 'eres tonto o abrazas farolas\n'],['pizza\n', 'sushi\n', 'donetes\n', 'hamburguesa\n', 'chuleton\n'],['fwefewf\n', 'kukukukukau\n', 'lol xd wtf \n', 'jajajaja :v\n','esto con franco no pasaba\n'],['gallina\n', 'cerdo\n', 'perro\n', 'gato\n', 'conejo\n', 'avestruz\n'],['tu puedes\n', 'querer es poder\n', 'vales lo que el oro\n', 'llegaras lejos\n', 'mucha mierda\n'],['kikiriki\n', 'muuuu\n', 'guau guau\n', 'miau miau\n', 'hihoooo\n', 'oink oink\n'],['la vida es corta\n', 'no queda bada entre tu y yo\n', 'mate a tu perro con el coche\n', 'no estes triste, la vida es una puta mierda si pero...\n']]
    sec=0
    while True:
        sleep(1)
        max_len= int(len(full_list[sec])-1)
        print(full_list[sec][random.randint(0, max_len)])
        sec += 1
        if sec == 10:
            sec=0

if __name__ == "__main__":
    main()