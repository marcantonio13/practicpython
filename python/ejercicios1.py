import math
#Area de un triangulo 

def area_triangulo(base,altura):
    return (base*altura)/2

print(area_triangulo(5,8))


#Area de un circulo 

def area_circulo(r):
    return math.pi*(r**2)
print(area_circulo(8))


#Relacion entre números si el primero es mayor 
#que el segundo regresa 1 si el segundo es mayor 
#primero regresa -1

def relacion_numeros(primero,segundo):
    if primero > segundo: 
        return 1
    elif primero < segundo: 
        return -1
    else:
        return 0
print(relacion_numeros(11,11))



#Separa listas en pares y impares 

def separar(lista):
    lista.sort()
    pares = []
    impares = []
    for n in lista: 
        if n % 2 == 0: 
            pares.append(n)
        else:
            impares.append(n)
    return pares , impares

pares, impares = separar([5,9,8,9,66,89,101])
print(pares)
print(impares)
    
