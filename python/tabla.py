import sys

if len(sys.argv) == 3: 
    try:
        filas = int(sys.argv[1])
        columnas = int(sys.argv[2])

        if 1 <= filas <= 9 and 1 <= columnas <= 9:
            for f in range(filas):
                for c in range(columnas):
                    print(" * ", end='')
                print()  # Salto de línea después de cada fila
        else:
            print("Error: filas o columnas incorrectas")
            print("Ejemplo: python tabla.py 5 5 (valores entre 1 y 9)")
    except ValueError:
        print("Error: Argumentos deben ser números enteros")
else: 
    print("Error de argumentos")
