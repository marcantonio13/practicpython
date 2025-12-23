import re
###   Metacarter un repeticiones * 

def buscar(patrones,texto):
    for patron in patrones: 
        print(re.findall(patron, texto))

patrones = ['hola', 'hla', 'hola']
texto = " hola  holaaa   hoooolaa    holalall    hla"

buscar(patrones,texto)


#####3    Metacaracter con * + 


texto = " hola  holaaa   hoooolaa    holalall    hla"
patrones = ['ho+','ho*','ho*la']
buscar(patrones,texto)

######3 Metacarater con {}

texto = " hola  holaaa   hoooolaa    holalall    hla"
patrones = ['ho{0}','ho{5}','ho{2}la']
buscar(patrones,texto)

#### metacarteres rangos de repeticioness 

texto = " hola  hooolaaa   hoooolaa    hoooooolalall    hla"
patrones = ['ho{0,2}','ho{2,5}','ho{3,10}la']
buscar(patrones,texto)




