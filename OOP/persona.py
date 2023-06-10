class Perro:
    # Constructor
    def __init__(self, n, r, c):
        self.nombre = n
        self.edad = 0
        self.color = c
        self.raza = r

    # Métodos
    def ladrar(self):
        print("{} está ladrando".format(self.nombre))

    def comer(self):
        print("{} está comiendo".format(self.nombre))

    def jugar(self):
        print("{} está jugando".format(self.nombre))

    # Setter / Getter

    def cambiar_nombre(self, nombre):
        self.nombre = nombre
        print("El perro ahora se llama {}".format(nombre))

    def set_edad(self, edad):
        self.edad = edad
        print("{} ahora tiene {} años".format(self.nombre, self.edad))

    def cumpleaños(self):
        self.edad += 1
        print("{} ahora tiene {} años".format(self.nombre, self.edad))


# Instanciar objetos
mi_perro = Perro("Tommy", "Labrador", "Blanco")
print(mi_perro.nombre)
mi_perro.comer()
mi_perro.cumpleaños()

mi_perro2 = Perro("Beethoven", "Dálmata", "Plomo")
print(mi_perro2.nombre)
mi_perro2.comer()