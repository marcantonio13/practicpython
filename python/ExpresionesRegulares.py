import re 


texto = "En esta cadena se encuentra una palabra magica"

re.search('magica',texto)

re.search('hola',texto)

palabra = 'magica'

encontrado = re.search(palabra,texto)

if encontrado is not None: 
    print("Se ha encontrado la palabra")
else:
    print("No se a encontrado la palabra")


#####

print(encontrado.start())
print(encontrado.end())
print(encontrado.span())
print(encontrado.string)



###

texto = "Hola mundo"
print(re.match('Hola',texto))

texto = "Vamos a dividir esta cadena"
print(re.split(' ',texto))


####



texto = "Hola amiga0"
print(re.sub('amigo','amiga',texto))
#####3

texto = "Hola adios hola hola hola"

print(re.findall('hola',texto))
print(len(re.findall('hola',texto)))

#####

texto = "hola adios hello bye"
print(re.findall("(hola|hello)",texto))
