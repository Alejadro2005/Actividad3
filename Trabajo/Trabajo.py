import math
class Vehiculo:
    def __init__(self,velocidad_maxima, kilometraje):

        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def mostrar(self):
        print("Punto",self.x, self.y)

    def mover(self,dx,dy):
        self.x += dx
        self.y += dy

    def calcular_distancia(self,otro_punto):
        return math.hypot(self.x - otro_punto.x, self.y - otro_punto.y)

