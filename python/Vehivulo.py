
class Vehiculo: 

    def __init__(self,color,ruedas):

        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return  "color {}  , ruedas {}" .format(self.color,self.ruedas)
    

class Coche(Vehiculo):
    def __init__(self, color, ruedas,velocidad,cilindrada):
        super().__init__(color,ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() +  " {}  km/hrs. ,  {} cc" .format(self.velocidad,self.cilindrada)


c = Coche("gris",
          "205/55 R16",
          206,1.6 )
print(c)
    