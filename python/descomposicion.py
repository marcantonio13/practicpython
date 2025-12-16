import sys

if len(sys.argv) == 2: 
    numero = int(sys.argv[1])
    if numero < 0 or numero > 99999999: 
        print("Numero incorrecto")
        print("El numero debe estar [1,99999999]")
    else: 
        cadena = str(numero)
        longitud = len(cadena)
        for i in range(longitud):
            print("{:04d}" .format(int(cadena[longitud -1 -i])*10 **i))

else:
    print("Argumentos incorrectos")