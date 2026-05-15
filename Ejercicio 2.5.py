from enum import Enum


class TipoCuenta(Enum):
    AHORROS = 1
    CORRIENTE = 2


class CuentaBancaria:
    def __init__(self, nombres_titular, apellidos_titular, numero_cuenta, tipo_cuenta):
        self.nombres_titular = nombres_titular
        self.apellidos_titular = apellidos_titular
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0

    def imprimir(self):
        print("\n--- Informacion de la cuenta bancaria ---")
        print(f"Nombres del titular: {self.nombres_titular}")
        print(f"Apellidos del titular: {self.apellidos_titular}")
        print(f"Numero de la cuenta bancaria: {self.numero_cuenta}")
        print(f"Tipo de cuenta: {self.tipo_cuenta.name}")
        print(f"Saldo: {self.saldo}")

    def consultar_saldo(self):
        return self.saldo

    def consignar(self, valor):
        self.saldo += valor

    def retirar(self, valor):
        if valor > self.saldo:
            print("No es posible realizar el retiro porque supera el saldo actual.")
        else:
            self.saldo -= valor


def solicitar_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("La entrada no puede estar vacia.")


def solicitar_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ingresar un numero entero valido.")


def solicitar_flotante(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Debe ingresar un valor numerico valido.")


def solicitar_tipo_cuenta():
    while True:
        print("1. Cuenta de ahorros")
        print("2. Cuenta corriente")
        opcion = input("Seleccione el tipo de cuenta: ").strip()
        if opcion == "1":
            return TipoCuenta.AHORROS
        if opcion == "2":
            return TipoCuenta.CORRIENTE
        print("Opcion invalida.")


if __name__ == "__main__":
    nombres = solicitar_texto("Nombres del titular: ")
    apellidos = solicitar_texto("Apellidos del titular: ")
    numero_cuenta = solicitar_entero("Numero de la cuenta bancaria: ")
    tipo_cuenta = solicitar_tipo_cuenta()

    cuenta = CuentaBancaria(nombres, apellidos, numero_cuenta, tipo_cuenta)

    print(f"Saldo inicial: {cuenta.consultar_saldo()}")

    valor_consignacion = solicitar_flotante("Valor a consignar: ")
    cuenta.consignar(valor_consignacion)
    print(f"Saldo despues de consignar: {cuenta.consultar_saldo()}")

    valor_retiro = solicitar_flotante("Valor a retirar mayor al saldo actual: ")
    cuenta.retirar(valor_retiro)
    print(f"Saldo despues del intento de retiro: {cuenta.consultar_saldo()}")

    valor_retiro_valido = solicitar_flotante("Valor a retirar valido: ")
    cuenta.retirar(valor_retiro_valido)
    print(f"Saldo final: {cuenta.consultar_saldo()}")

    cuenta.imprimir()
