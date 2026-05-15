from enum import Enum


class TipoCombustible(Enum):

    GASOLINA = 1
    BIOETANOL = 2
    DIESEL = 3
    BIODIESEL = 4
    GAS_NATURAL = 5


class TipoAutomovil(Enum):

    CIUDAD = 1
    SUBCOMPACTO = 2
    COMPACTO = 3
    FAMILIAR = 4
    EJECUTIVO = 5
    SUV = 6


class Color(Enum):

    BLANCO = 1
    NEGRO = 2
    ROJO = 3
    NARANJA = 4
    AMARILLO = 5
    VERDE = 6
    AZUL = 7
    VIOLETA = 8


class Automovil:

    def __init__(
        self,
        marca: str,
        modelo: int,
        motor: float,
        tipo_combustible: TipoCombustible,
        tipo_automovil: TipoAutomovil,
        numero_puertas: int,
        cantidad_asientos: int,
        velocidad_maxima: float,
        color: Color,
    ) -> None:
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.numero_puertas = numero_puertas
        self.cantidad_asientos = cantidad_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.velocidad_actual = 0.0

    def get_marca(self) -> str:
        return self.marca

    def set_marca(self, marca: str) -> None:
        self.marca = marca

    def get_modelo(self) -> int:
        return self.modelo

    def set_modelo(self, modelo: int) -> None:
        self.modelo = modelo

    def get_motor(self) -> float:
        return self.motor

    def set_motor(self, motor: float) -> None:
        self.motor = motor

    def get_tipo_combustible(self) -> TipoCombustible:
        return self.tipo_combustible

    def set_tipo_combustible(self, tipo_combustible: TipoCombustible) -> None:
        self.tipo_combustible = tipo_combustible

    def get_tipo_automovil(self) -> TipoAutomovil:
        return self.tipo_automovil

    def set_tipo_automovil(self, tipo_automovil: TipoAutomovil) -> None:
        self.tipo_automovil = tipo_automovil

    def get_numero_puertas(self) -> int:
        return self.numero_puertas

    def set_numero_puertas(self, numero_puertas: int) -> None:
        self.numero_puertas = numero_puertas

    def get_cantidad_asientos(self) -> int:
        return self.cantidad_asientos

    def set_cantidad_asientos(self, cantidad_asientos: int) -> None:
        self.cantidad_asientos = cantidad_asientos

    def get_velocidad_maxima(self) -> float:
        return self.velocidad_maxima

    def set_velocidad_maxima(self, velocidad_maxima: float) -> None:
        self.velocidad_maxima = velocidad_maxima

    def get_color(self) -> Color:
        return self.color

    def set_color(self, color: Color) -> None:
        self.color = color

    def get_velocidad_actual(self) -> float:
        return self.velocidad_actual

    def set_velocidad_actual(self, velocidad_actual: float) -> None:
        self.velocidad_actual = velocidad_actual

    def acelerar(self, incremento: float) -> None:
        nueva_velocidad = self.velocidad_actual + incremento
        if nueva_velocidad > self.velocidad_maxima:
            print(
                "Aviso: la velocidad supera la maxima permitida. "
                "Se ajustara a la velocidad maxima."
            )
            self.velocidad_actual = self.velocidad_maxima
        else:
            self.velocidad_actual = nueva_velocidad

    def desacelerar(self, decremento: float) -> None:
        nueva_velocidad = self.velocidad_actual - decremento
        if nueva_velocidad < 0:
            print("Aviso: la velocidad no puede ser negativa. Se ajustara a 0.")
            self.velocidad_actual = 0.0
        else:
            self.velocidad_actual = nueva_velocidad

    def frenar(self) -> None:
        self.velocidad_actual = 0.0

    def calcular_tiempo_llegada(self, distancia_km: float):
        if self.velocidad_actual == 0:
            print("Error: la velocidad actual es 0, no es posible calcular el tiempo de llegada.")
            return None
        return distancia_km / self.velocidad_actual

    def imprimir(self) -> None:
        print("\n--- Informacion del automovil ---")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Motor: {self.motor} litros")
        print(f"Tipo de combustible: {self.tipo_combustible.name}")
        print(f"Tipo de automovil: {self.tipo_automovil.name}")
        print(f"Numero de puertas: {self.numero_puertas}")
        print(f"Cantidad de asientos: {self.cantidad_asientos}")
        print(f"Velocidad maxima: {self.velocidad_maxima} km/h")
        print(f"Color: {self.color.name}")
        print(f"Velocidad actual: {self.velocidad_actual} km/h")


def solicitar_texto(mensaje: str) -> str:
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("La entrada no puede estar vacia. Intente de nuevo.")


def solicitar_entero(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada invalida. Debe ingresar un numero entero.")


def solicitar_flotante(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada invalida. Debe ingresar un numero decimal.")


def solicitar_enum(mensaje: str, enum_clase: Enum):
    opciones = list(enum_clase)
    while True:
        for opcion in opciones:
            print(f"{opcion.value}. {opcion.name}")
        try:
            seleccion = int(input(mensaje))
            for opcion in opciones:
                if opcion.value == seleccion:
                    return opcion
            print("Opcion invalida. Intente nuevamente.")
        except ValueError:
            print("Entrada invalida. Debe seleccionar un numero.")


if __name__ == "__main__":
    print("Ingrese los datos del automovil:\n")

    marca = solicitar_texto("Marca: ")
    modelo = solicitar_entero("Modelo (año): ")
    motor = solicitar_flotante("Motor (litros): ")

    print("\nSeleccione el tipo de combustible:")
    tipo_combustible = solicitar_enum("Opcion: ", TipoCombustible)

    print("\nSeleccione el tipo de automovil:")
    tipo_automovil = solicitar_enum("Opcion: ", TipoAutomovil)

    numero_puertas = solicitar_entero("Numero de puertas: ")
    cantidad_asientos = solicitar_entero("Cantidad de asientos: ")
    velocidad_maxima = solicitar_flotante("Velocidad maxima (km/h): ")

    print("\nSeleccione el color:")
    color = solicitar_enum("Opcion: ", Color)

    automovil = Automovil(
        marca,
        modelo,
        motor,
        tipo_combustible,
        tipo_automovil,
        numero_puertas,
        cantidad_asientos,
        velocidad_maxima,
        color,
    )

    automovil.acelerar(100)
    print(f"Velocidad actual despues de acelerar a 100 km/h: {automovil.velocidad_actual} km/h")

    automovil.acelerar(20)
    print(f"Velocidad actual despues de acelerar 20 km/h mas: {automovil.velocidad_actual} km/h")

    automovil.desacelerar(50)
    print(f"Velocidad actual despues de desacelerar 50 km/h: {automovil.velocidad_actual} km/h")

    automovil.frenar()
    print(f"Velocidad actual despues de frenar: {automovil.velocidad_actual} km/h")

    automovil.imprimir()