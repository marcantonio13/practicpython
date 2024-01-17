
print("Sistema para calcular el promedio de un alumno")
nombre = input("Para comenzar, ¿Cual es tú nombre?: ")
cal_mat = int(input("¿Cuál es tú calificación de matemáticas?: "))
cal_qui = int(input("¿Cuál es tú calificación de quimica?: "))
cal_bio = int(input("¿Cuál es tú calificación de biología?: "))

promedio = (cal_mat + cal_qui + cal_bio)/3

if promedio >= 6 :
    print('Felicidades' + nombre + ' "pasaste" el semestre tu calificación es de :',int(promedio))
else :
    print(" 'Reprobaste' ")

print("Fin.")
