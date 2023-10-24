### Ejercicio 1 ###

# 1.Crea una variable 'temp' con la temperatura actual en grados celsius(por ejemplo: 25)
# 2.Creo una variable "viento" con la velocidad del viento en km/h (por ejemplo: 10)
# 3.Usando una estructura "if-elif-else", determina si el clima es agradable, fresco o frio
# 4.Si la temperatura es mayor a 25 grados Celsius y la velocidad del viento es menor a 5 km/h, imprimir "Clima Agradable"
# 5.Si la temperatura està entre 20 y 25 grados Celsius o la velocidad del viento està enrte 5 y 15 km/h, imprimir "Cliente Fresco"
# 6.Si la temperatura es menor a 20 grados Celsius o la velocidad del viento es mayor a 15 km/h, imprimir "Clima Frio"

temp : int = 25
viento : int = 10

if temp > 25 and viento < 5:
    print("Clima Agradable")
elif (temp >= 20 and temp <= 25) or (viento >= 5 and viento <= 15):
    print("Clima Fresco")
elif temp < 20 or viento > 15:
    print("Clima Frio")
else:
    print("Clima no agradable")

### Ejercicio 2 ###

# 1.Crea una variable "edad" y asignale tu edad actual.
# 2.Crea una variable "tiene_permiso" y asignale "True" si tienes permiso para coducir, "False" en caso contrario.
# 3.Usando una estructura "if-elif-else", imprime un mensaje diferente dependiendo de si tienes permiso para conducir o no
#   3.1. Si tienes permiso para conducir y tu edad es mayor o igual a 21, imprime "Puedes conducir y ademas eres mayor de edad"
#   3.2. Si tienes permiso para conducir pèro tu edad es meor a 21, imprime "Puedes conducir pero aùn eres menor de edad"
#   3.3  No tienes permiso para conducir, Imprime "No tienes permiso para conducir"

edad : int = 24
tpermiso : bool = True

if tpermiso and edad >= 21:
    print("Pueds conducir y ademas eres mayor de edad")
elif tpermiso and edad < 21:
    print("Puedes conducir pero aùn eres menor de edad")
elif not tpermiso:
    print("No tiene permiso para conducir")



