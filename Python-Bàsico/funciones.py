def saludar():
    if 7 > 5:
        print("es mayor")
    else:
        print("es menor")
saludar()



def saludos(nombre,edad):
    print(nombre,edad)

saludos("Isaias",17)





def sumar(variable1, variable2):
    return variable1 + variable2

print(sumar(6,17))


def evaluar(x,y):
    if sumar(x,y) > 20:
        return  True
    else:
        return False
print(evaluar(5,17))