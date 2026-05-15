class Caracteristicas:
    def __init__(self, nombre, apellidos, numero_documento,
                 anio_nacimiento, pais, genero):

        self.nombre = nombre
        self.apellidos = apellidos
        self.numero_documento = numero_documento
        self.anio_nacimiento = anio_nacimiento
        self.pais = pais
        self.genero = genero

    def __str__(self):
        return (
            f"{self.nombre} {self.apellidos}\n"
            f"Número de documento: {self.numero_documento}\n"
            f"Año de nacimiento: {self.anio_nacimiento}\n"
            f"País de nacimiento: {self.pais}\n"
            f"Género: {self.genero}"
        )


class Persona:
    def __init__(self, nombre, apellidos, numero_documento,
                 anio_nacimiento, pais, genero):

        self.caracteristicas = Caracteristicas(
            nombre,
            apellidos,
            numero_documento,
            anio_nacimiento,
            pais,
            genero
        )


nombre = input("Digite su nombre: ")
apellidos = input("Digite sus apellidos: ")
numero_documento = input("Digite su documento: ")
anio_nacimiento = input("Digite su año de nacimiento: ")
pais = input("Digite su país de origen: ")
genero = input("Digite su género: ")

persona = Persona(
    nombre,
    apellidos,
    numero_documento,
    anio_nacimiento,
    pais,
    genero
)

print(persona.caracteristicas)