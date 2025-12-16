from io import open
2
fichero = open(r"C:\Users\anton\OneDrive\Documentos\Python\personas.txt","r",encoding="utf8")
lineas = fichero.readlines()
fichero.close()

personas = []

for linea in lineas: 
    liena = linea.replace("\n","")
    campos = linea.split(";")
    persona = {"id":campos[0],"nombre":campos[1],"apellidos":campos[2],"nacimiento":campos[3]}
    personas.append(persona)

for p in personas:
    print("id={}  {}   {}  =>  {}".format(p['id'],p['nombre'], p['apellidos'],p['nacimiento']))