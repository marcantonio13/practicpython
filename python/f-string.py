#Cadena contexto 
nombre = "Hector"
cadena = f"Hola {nombre}"
print(cadena)


#Suma 

a, b = 15,30

print(f"La suma de {a} + {b} es igaul a {a+b}")


#Diccionario 

numero = { "uno":1, "dos":2 , "tres":3}

print(f"El núemro dos es {numero['dos']}")



#Aliniamientos 

texto = "Hola mundo"

print(f"{texto:40}") # Aliniacion 40 casracteres Izquierda
print(f"{texto:>40}") #Aliniacion 40 carateres derecha 
print(f"{texto:<40}") # Aliniacipn 40 caracteres Izquierda 
print(f"{texto:^40}") # Aliniación 40 carateres al centro 


