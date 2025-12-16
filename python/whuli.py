while(True):
    try: 
        n = float(input("Introduce un numero: "))
        m = float(input("introduce otro número"))
        print("{}/{} = {}" .format(n,m,n/m))
    except: 
        print("A ocurrido un erro")
    else: 
        print("Todo funciona correctamente")
        break
    finally: 
        print("fin de la interacción")

