# && AND(el resultado es verdadero si ambas expresiones o mas son verdaderas)#
# || OR(el resultado es verdadero si alguna expresión es verdadera)#
# NOT(el resultado invierte la condición de la expresión)#

a = 6 > 4 and 7 > 3 and "hola" == "hola"

a = 20 >= 11  or 7 < 4

a = not False

print (a)

#Condición IF
#Permite que un programa ejecute siertas accione
#siempre y cuando la condicíón  se cumpla

edad = 15

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")


precio = 21 
edad = 18

if precio == 20 and edad >=18:
    print("Es valor es igual ")
else:
    print("Uno de los 2 es falso")




