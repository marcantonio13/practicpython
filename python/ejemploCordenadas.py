import math

class Punto : 
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return " ({} , {})" .format(self.x,self.y)
    
    
    def cuadrante(self):
        if self.x > 0 and self.y >0: 
            print("{}  Estamos en el primer cuadrante" .format(self))
        elif self.x < 0 and self.y > 0: 
            print("{} Estamos en el segundo cuadrante" .format(self) ) 
        elif self.x < 0 and self.y < 0: 
            print("{} Estamos en el tercer cuadrante" .format(self) )
        elif self.x > 0 and  self.y < 0:
            print(" {} Estamos en el cuarto cuadrante" .format(self) )
        else:
            print("{} se encuentra en el origen" .format(self))
         

    def  vector(self,p): 
        print("El vector entre {} y {} es ({} , {} ) " .format(self,p ,p.x - self.x, p.y -self.y))


    def distancia(self,p):
        d = math.sqrt((p.x -self.x)**2 + (p.y-self.y)**2)
        print("La distancia entre {} y {}  es {}. " .format(self,p,d))



# Se crean los punto 
A = Punto(8,9)
B = Punto(-10,59)
C = Punto (-5,-9)
D = Punto(13,-16)
E = Punto(0,0)


A.cuadrante()
B.cuadrante()
C.cuadrante()
D.cuadrante()
E.cuadrante()

A.vector(B)
B.vector(C)
D.vector(E)

A.distancia(E)
B.distancia(C)
D.distancia(A)