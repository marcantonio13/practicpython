#Inicio del programa
print("""
=======================================================
    DETERMINACIÓN DE DIAS DE VACACIONES DE EMPLEADOS 
=======================================================

""")

nombre = input("Dame tu nombre: ")
clave  = int(input("Dame tu clave de empleado  1 , 2 ó 3:  "))
years_laborados = int(input("Dame los números de años laborados en la empresa: "))

if clave == 1:
    if years_laborados == 1 and years_laborados < 2:
        print("Le corresponden Sr(a) ",nombre, "6 dias de vacaciones. \n")   
    elif years_laborados >= 2 and years_laborados <= 6:
        print("Le corresponden Sr(a) ",nombre, "14 dias de vacaciones \n")
    elif years_laborados >= 7:
        print("Le corresponden Sr(a) ", nombre, "20 dias de vacaciones \n")
    else:
        print("Sin derecho a vacaciones \n")
        

elif clave == 2:
     if years_laborados == 1 and years_laborados < 2:
        print("Le corresponden Sr(a) ",nombre," 7 dias de vacaciones. \n")   
     elif years_laborados >= 2 and years_laborados <= 6:
        print("Le corresponden Sr(a) ",nombre," 15 dias de vacaciones")
     elif years_laborados >= 7:
        print("Le corresponden 22 dias de vacaciones")
     else:
        print("Sin derecho a vacaciones")
     

elif clave == 3:
     if years_laborados == 1 and years_laborados < 2:
        print("Le corresponden Sr(a) ", nombre," 10 dias de vacaciones. \n")   
     elif years_laborados >= 2 and years_laborados <= 6:
        print("Le corresponden Sr(a) ",nombre," 20 dias de vacaciones")
     elif years_laborados >= 7:
        print("Le corresponden Sr(a) ",nombre," 30 dias de vacaciones")
     else:
        print("Sin derecho a vacaciones")
     

else:
    print("La clave no existe. \n")
