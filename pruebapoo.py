class Rectangulo:
    def __init__(self,longitud,ancho):
        self.longitud=longitud
        self.ancho=ancho

    def calcular_area(self):
        self.area=self.longitud*self.ancho
      return area 
    
    def calcular_perimetro(self):
        self.perimetro=(self.longitud+self.ancho)*2
       return perimetro
    
obj1= Rectangulo(6,5)
print(obj1.calcular_area())
print(obj1.calcular_perimetro())        