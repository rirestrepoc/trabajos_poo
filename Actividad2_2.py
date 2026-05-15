class caracteristicas:
    def __init__(self, nombre, satelites, masa, volumen,diametro, distancia_media_sol,tipo_planeta,observable,periodo_orbital,periodo_rotacion):
        self.nombre = nombre
        self.satelites = satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_media_sol = distancia_media_sol
        self.tipo_planeta = tipo_planeta
        if observable=="si" or observable=="true":
            self.observable = True
        else:
            self.observable = False
        self.periodo_orbital = periodo_orbital
        self.periodo_rotacion = periodo_rotacion
    def __str__(self):
        return f'El nombre es {self.nombre}, tiene {self.satelites} satélites, su masa es {self.masa} kg, su volumen es {self.volumen} km³, su diámetro es {self.diametro} km, su distancia media al Sol es {self.distancia_media_sol} millones de km, su tipo de planeta es {self.tipo_planeta}, es observable: {self.observable}, su período orbital es {self.periodo_orbital} años y su período de rotación es {self.periodo_rotacion} días.'
nombre=input("digite su nombre")
satelites=int(input("digite sus satelites"))
masa=float(input("digite su masa"))
volumen=float(input("digite su volumen"))
diametro=int(input("digite su diametro"))
distancia_media_sol=int(input("digite su distancia_media_sol"))
tipo_planeta=input("digite su tipo_planeta")
observable=input("digite si es observable").strip().lower()
periodo_orbital=float(input("digite su periodo_orbital"))
periodo_rotacion=float(input("digite su periodo_rotacion"))
hola=caracteristicas(nombre, satelites, masa, volumen,diametro, distancia_media_sol,tipo_planeta, observable,periodo_orbital, periodo_rotacion)
print(hola)