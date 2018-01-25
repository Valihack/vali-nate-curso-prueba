texto=input("Por favor introduzca un texto (El texto debe acabar con un punto '.'): ")
lista_palabras=[]
contador=0
i=0
lista_final=[]
texto=" "+texto+"."
while i < len(texto):
    caracter=texto[i]
    if caracter == " " or caracter=="." or caracter=="," or caracter=="-" or caracter==":" or caracter==";":
        lista_palabras.append(texto[contador:i])
        contador=i
        i+=1
    i+=1
numero_de_veces_que_se_repite=0
indice=0
repetida = 0
i=0
r=0
while indice<len(lista_palabras):
    while i<len(lista_final):
        if lista_palabras[indice] == lista_final[i][0]:
            repetida=1
        i+=1
    if repetida==0:
        for palabra in lista_palabras:
            if palabra == lista_palabras[indice]:
                numero_de_veces_que_se_repite+=1
        lista_final.append([lista_palabras[indice], numero_de_veces_que_se_repite])
    numero_de_veces_que_se_repite=0
    repetida = 0
    indice+=1
    i=0
i=1
while i < len(lista_final):
    print("La palabra {} esta {} repetida".format(lista_final[i][0],lista_final[i][1]))
    i+=1

