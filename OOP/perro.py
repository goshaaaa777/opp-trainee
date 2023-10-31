from mascota import Mascota

class Perro(Mascota):
    __color_pelo : str
    __raza_ : str
    __trofeos_ganados : dict

    def __init__(self, nombre, puntos_salud, nivel, edad, color_pelo, raza) -> None:
        super().__init__(nombre,puntos_salud, nivel,edad)
        self.__color_pelo = color_pelo
        self.__raza = raza
        self.__trofeos_ganados = {'Internacional': 0, 'Nacional': 0, 'Internacional':0}

    def get_color_pelo(self) -> str:
        return self.__color_pelo
    
    def set_color_pelo(self, value):
        self.__color_pelo = value

    def get_raza(self) -> str:
        return self.__raza
    
    def set_raza(self, value):
        self.__raza = value
    
    def get_troferos_ganados(self) -> dict:
        return self.__trofeos_ganados.copy()
    
    #def set_trofeos_ganados(self, value):
       #self.__trofeos_ganados = value.copy()

    def ganar_torneo(self, tipo_torneo: str) -> None:
        super().ganar_torneo(tipo_torneo)
        if tipo_torneo in self.__trofeos_ganados.keys():
            self.__trofeos_ganados[tipo_torneo] += 1

scott : Perro = Perro('Scott',100,1,1,'Blanco','Labrador')
scott.ganar_torneo('Internacional')
print(scott.get_nivel())
print(scott.get_troferos_ganados())