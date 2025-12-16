
class Producto: 
    def __init__(self,referencia,nombre,pvp,descripcion):
        self.referencia = referencia
    
        self.nombre = nombre 
        self.pvp = pvp
        self.descripcion = descripcion


    def __str__(self):
        return """ 
            REFERENCIA {} \t
            NOMBRE  {} \t
            PVP {} \t
            DESCRIPCIÓN {} \t 

                """ .format(self.referencia,self.nombre,self.pvp,self.descripcion)


class Adorno(Producto):
    pass

a =Adorno(5899,"Celular",30,"Es un telefono nuevo")
print(a)




class Alimento(Producto):
    productor = ""
    distribuidor = ""

    def __str__(self):
        return """
            REFERENCIA \t {}
            NOMBRE  \t {}
            PVP \t {}
            DESCRIPCIÓN  \t{}
            PRODUCTOR  \t{}
            DISTRIBUIDOR  \t{}

                """ .format(self.referencia,
                            self.nombre,
                            self.pvp,
                            self.descripcion,
                            self.productor,
                            self.distribuidor)
    




al = Alimento(9098,
              "Chocolaton",
              55,
              "Es un chocolate Méxicano",)
al.productor = "La vaca"
al.distribuidor =" La loba"

print(al)

productos = [a,al]  

for p in productos:
    print(p,"\n")



print(This)

        