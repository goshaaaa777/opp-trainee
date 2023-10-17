class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

celular1 = Celular("Samsung","S23","48MP")
celular2 = Celular("Iphone","12","88MP")

print(celular2.marca)