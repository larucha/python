class Rectangulo:
    def __init__(self,longitud,ancho):
        self.longitud=longitud
        self.ancho=ancho

    def calcular_area(self):
        self.longitud=self.longitud*self.ancho
        return self.area
    
    def calcular_perimetro(self):
        self.perimetro=self.longitud+self.ancho
        return self.perimetro
    
    obj1= Rectangulo(6,3)
    print(obj1.calcular_area())
    print(obj1.calcular_perimetro())        