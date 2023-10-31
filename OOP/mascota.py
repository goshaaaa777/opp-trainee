
#Implementacion de la clase mascota para un videojuego de animales.

class Mascota:
#Atributos de la clase 
    __nombre : str
    __puntos_salud : int
    __nivel : int
    __edad : int

#Constructor de la clase
    
    def __init__(self, nombre, puntos_salud,nivel,edad) -> None:
        self.__nombre = nombre
        self.__puntos_salud = puntos_salud
        self.__nivel = nivel
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, value):
        self.__nombre = value
    def get_puntos_salud(self):
        return self.__puntos_salud
    def set_puntos_salud(self, value):
        self.__puntos_salud = value
    def get_nivel(self):
        return self.__nivel
    def set_nivel(self, value):
        self.__nivel = value
    def get_edad(self):
        return self.__edad
    def set_edad(self, value):
        self.__edad = value

    def alimentar(self, comida : str) -> None:
        if comida == 'comida_normal':
            self.__puntos_salud += 10
        elif comida == 'comida_buena':
            self.__puntos_salud += 20
        elif comida == 'comida_genial':
            self.__puntos_salud +=30
        
        print(f"Me siento màs fuerte y tengo {self.__puntos_salud} puntos de salud")
    
    def ganar_torneo(self, tipo_torneo : str) -> None:
        if tipo_torneo == 'Regional':
            self.__nivel += 1
        elif tipo_torneo == 'Nacional':
            self.__nivel += 2
        elif tipo_torneo == 'Internacional':
            self.__nivel += 3