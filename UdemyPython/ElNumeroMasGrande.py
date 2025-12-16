print("""
============================================================================
    Programa que verifica ¿Cúal es el número mas grande de tres números?
============================================================================
""")

numero_uno = int(input("Dame el primer número: "))
numero_dos = int(input("Dame el segundo número: "))
numero_tres = int(input("Dame el tercero número: "))

if numero_uno > numero_dos  and numero_uno > numero_tres:
    print("El ",numero_uno, " es el número mas grande de los tres")
elif numero_dos > numero_uno and numero_dos > numero_tres:
    print("El ",numero_dos," es el número mas grande de los tres")
elif numero_tres > numero_uno and numero_tres > numero_dos:
     print("El ",numero_tres, " es el número mas grande de los tres")
else:
    print("A acurrido un error")
    
