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

class Rectangulo:
    def __init__(self,esquina1,esquina2):
        self.esquina1 = esquina1
        self.esquina2 = esquina2

    def calcular_perimetro(self):
        largo = abs(self.esquina1.x - self.esquina2.x)
        ancho = abs(self.esquina1.y - self.esquina2.y)
        perimetro = 2 * (largo + ancho)
        print("El perímetro del rectángulo es:",perimetro,"unidades")
        return perimetro

    def calcular_area(self):
        largo = abs(self.esquina1.x - self.esquina2.x)
        ancho = abs(self.esquina1.y - self.esquina2.y)
        area = largo * ancho
        print("El área del rectángulo es:",area,"unidades cuadradas")
        return area

    def es_cuadrado(self):
        largo = abs(self.esquina1.x - self.esquina2.x)
        ancho = abs(self.esquina1.y - self.esquina2.y)
        return largo == ancho

class Circulo:
    def __init__(self,centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio **2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def punto_pertenece(self, punto):
        distancia = math.hypot(self.centro.x - punto.x, self.centro.y - punto.y)
        return distancia <= self.radio

class Carta:
    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

    PINTAS = ('Diamantes', 'Corazones', 'Treboles', 'Pintas')

