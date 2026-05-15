import math


# =========================
# Clase Circulo
# =========================
class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio


# =========================
# Clase Rectangulo
# =========================
class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return (2 * self.base) + (2 * self.altura)


# =========================
# Clase Cuadrado
# =========================
class Cuadrado:

    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

    def calcular_perimetro(self):
        return 4 * self.lado


# =========================
# Clase TrianguloRectangulo
# =========================
class TrianguloRectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_hipotenusa(self):
        return math.sqrt(
            (self.base ** 2) + (self.altura ** 2)
        )

    def calcular_perimetro(self):
        return (
            self.base +
            self.altura +
            self.calcular_hipotenusa()
        )

    def determinar_tipo_triangulo(self):

        hipotenusa = self.calcular_hipotenusa()

        if (
            self.base == self.altura and
            self.base == hipotenusa
        ):

            return "Equilatero"

        elif (
            self.base != self.altura and
            self.base != hipotenusa and
            self.altura != hipotenusa
        ):

            return "Escaleno"

        else:

            return "Isosceles"


# =========================
# Programa principal
# =========================

print("===== CIRCULO =====")
radio = float(input("Ingrese el radio del circulo: "))
figura1 = Circulo(radio)

print("Area =", figura1.calcular_area())
print("Perimetro =", figura1.calcular_perimetro())

print()

print("===== RECTANGULO =====")
base_rect = float(input("Ingrese la base del rectangulo: "))
altura_rect = float(input("Ingrese la altura del rectangulo: "))

figura2 = Rectangulo(base_rect, altura_rect)

print("Area =", figura2.calcular_area())
print("Perimetro =", figura2.calcular_perimetro())

print()

print("===== CUADRADO =====")
lado = float(input("Ingrese el lado del cuadrado: "))

figura3 = Cuadrado(lado)

print("Area =", figura3.calcular_area())
print("Perimetro =", figura3.calcular_perimetro())

print()

print("===== TRIANGULO RECTANGULO =====")
base_tri = float(input("Ingrese la base del triangulo: "))
altura_tri = float(input("Ingrese la altura del triangulo: "))

figura4 = TrianguloRectangulo(base_tri, altura_tri)

print("Area =", figura4.calcular_area())
print("Perimetro =", figura4.calcular_perimetro())
print("Hipotenusa =", figura4.calcular_hipotenusa())
print("Tipo de triangulo =", figura4.determinar_tipo_triangulo())