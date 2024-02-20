import math
class Vehiculo:
    def __int__(self,velocidad_maxima, kilometraje):

        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

class Punto:
    def __int__(self,x,y):
        self.x = x
        self.y = y

    def mostrar(self):
        print("Punto",self.x, self.y)

    def mover(self,dx,dy):
        self.x += dx
        self.y += dy
