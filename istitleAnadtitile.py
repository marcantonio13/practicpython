#Metodo stitle and title

first_name = input("Nombre: ")
last_name = input("Apellido: ")
full_name = f"{first_name} {last_name}"

print(f"¿El formato del método titile() se ha aplicado?: {full_name.istitle()} \n")
print(f"Aplicando el método titile(): {full_name.title()}")
print(f"Volveremos a imprimir el nombre: {full_name} \n")

full_name = full_name.title()
print(f"¿El formato del método titile() se ha aplicado?: {full_name.istitle()} ")
print(f"Aplicando el método titile(): {full_name.title()}")
print(f"Volveremos a imprimir el nombre: {full_name}")
