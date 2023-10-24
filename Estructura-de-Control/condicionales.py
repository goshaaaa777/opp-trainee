# Condicional booleano
valor_booleano = True

if valor_booleano:
    print("El valor es verdadero")

# Condicional booleano con else

if valor_booleano:
    print("El valor es verdadero")
else:
    print("El valor no es verdadero")

# Condicional numerico
edad = 10

if edad >= 18 and edad <= 80:
    print("Enhorabuena puedes conducir un carro")
else:
    print("No cumples la edad necesaria para coducir un carro")

# Condicional numerico con elif

dinero = 5
if dinero > 1000:
    print("Eres rico")
elif dinero > 500:
    print("Tienes algo de dinero")
elif dinero > 100:
    print("Hay que seguir estudiando")
else:
    print("eres pobre")

# Condicional con strings
nombre = "antaisaiasgs"

if nombre == "antaisaiasgs":
    print("Tu nombre existe en la bd")
else:
    print("Tu usuario no se ha creado")

# Condicional con listas

lista = ['arturo', 'pepe', 'maria']
input_login = 'arturo'

if input_login in lista:
    print("Usuario encontrado en la lista")
else:
    print("No tenemos tu usuario, registrate")

# Comprobar si una lista està vacìa

if lista:
    print(lista[0])
else:
    print("No hay elementos en la lista")

# Condicional inline

dinero = 800
estatus_economico = 'clase alta' if dinero > 1000 else 'clase media' if dinero > 500 else 'clase baja'
print(estatus_economico)