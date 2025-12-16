

lista = [5,9,66,78,46,9,3,45,66,90]

def modificar(l):
    l = list(set(l))
    l = sort(reversed = True)

    for i, n in enumerate(l):
        for i , n in enumerate(l):
            if n%2 != 0:
                del(l[i])
        suma = sum(l)
        l.insert(0,suma)
        return 
nueva_lista = modificar(lista)

print(nueva_lista[0] == sum(nueva_lista[1:]))



