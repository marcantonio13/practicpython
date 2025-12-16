"""un dia el viento soplaba con fuerzas coo se mueve aquellas baderol
-dijo un monje#lo que se mueve es el viento -responde otro monje#ni las 
bnaderolas nie le viento, lo que se mueve son vuestras mentes -dijo el maestro
"""

#Ordenar el texto como poema 

texto = "un dia el viento soplaba con fuerzas como se mueve aquellas baderol -dijo un monje#lo que se mueve es el viento -responde otro monje#ni las bnaderolas nie le viento, lo que se mueve son vuestras mentes -dijo el maestro"

lineas = texto.split("#")

for i , linea in enumerate(lineas):
    lineas[i] =lineas.capitalize()
    if i == 0:
        lineas[i] = lineas[i] + "..."
        lineas[i] = " - " + lineas[i] 
    print(lineas)

