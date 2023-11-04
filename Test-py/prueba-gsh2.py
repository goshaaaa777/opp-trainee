for x in range(2,17,2):
    print(f"El valor que tiene nuestro bucle for es {x}")


colores = ["rojo","azul","verde","amarillo"]

print("---LISTADO DE COLORES---")

for color in colores:
    if color == "azul" or color =="verde":
        print(f"Se ha saltado este valor")
        continue
    print(f"-Color {color}.")
    

for x in range(7,14):
    print(f"El valor que tiene nuestro bucle for es {x}")


i = 7

while i <= 14:
    print(f"El vaor del bucle es {i}.")
    i += 1


lista_numeros = [10,5,14,123,34,78,12,11,99,42,10]

lista_numeros.sort()

for i in lista_numeros:
    if i == 10:
        continue
    elif i == 123:
        break
    else:
        print(f"El valor del elemento es {i}")

for i in lista_numeros:
    if i == 10:
        continue
    elif i == 12:
        break
    print(f"El valor del elemento es {i}")