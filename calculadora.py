print("""
==========================================================
        CALCULADORA MENU DE OPCIONES
==========================================================
""")

print("""
1.- Suma
2.- Resta
3.- Multiplicación
4.- División
5.- División Entera
6.- Exponente
7.- Modulo o resto
""")

opc_menu = int(input("Introduce la opción deseada:  "))

if opc_menu == 1:
    print("Elegiste Suma \n")
    numero = int(input("Introduce el primer número: "))
    numero += int(input("Introduce el segundo número: "))
    print("El resultado de la Suma es: ",numero)
elif opc_menu ==2:
    print("Elegiste Resta \n")
    numero = int(input("Introduce el primer número: "))
    numero -= int(input("Introduce el segundo número: "))
    print("El resultado de la Resta es: ",numero)
elif opc_menu ==3:
    print("Elegiste Multiplicación \n")
    numero = int(input("Introduce el primer número: "))
    numero *= int(input("Introduce el segundo número: "))
    print("El resultado de la Multiplicación es: ",numero)
elif opc_menu ==4:
    print("Elegiste División \n")
    numero = int(input("Introduce el  número Numerados: "))
    numero /= int(input("Introduce el número Denominador: "))
    print("El resultado de la División es: ",numero)
elif opc_menu ==5:
    print("Elegiste División entera \n")
    numero = int(input("Introduce el número Numerados: "))
    numero //= int(input("Introduce el Expon: "))
    print("El resultado de la División entera es: ",numero)
elif opc_menu ==6:
    print("Elegiste Exponente \n")
    numero = int(input("Introduce el número Base: "))
    numero **= int(input("Introduce el número Denominador: "))
    print("El resultado del Exponente es: ",numero)
elif opc_menu ==7:
    print("Elegiste Modulo \n")
    numero = int(input("Introduce el número Base: "))
    numero %= int(input("Introduce el Exponente: "))
    print("El resultado del Modulo es: ",numero)
else:
    print("La opción elegida no existe,vulave a intentar")
    
    


