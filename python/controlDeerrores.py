colores = ["verde","rojo","azul","blanco"]
try:
    colores ["morado"]
except TypeError: 
    print("No se encuntra este color en la lista")



#Añadir elementos a lista y cambiar mensjae de erro 

elementos = [1,5,7]

def anadir_una_vez(lista,el): 
    try:
        if el in lista:
            raise ValueError
        else: 
            lista.append(el)
    except: 
        print("El elemento se encuntra duplicado en la lista")

anadir_una_vez(elementos,45)
anadir_una_vez(elementos,5)
anadir_una_vez(elementos,"Hola")

print(elementos)
