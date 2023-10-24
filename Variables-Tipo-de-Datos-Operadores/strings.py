#Longitud de un String
saludo = "hola mundo"
longitud_sludo = len(saludo) #calcular saludo

#Quitar espacios en blanco de al principioy y final de un string
string_espacios = "         esto es un string con espacios en blanco           "
string_sin_espacio = string_espacios.strip()

#Reemplazar partes de un strin por otro
mensaje_cifrado = "ESTO|ES|UN|MENSAJE|CIFRADO"
mensaje_decifrado = mensaje_cifrado.replace("|", " ")

#Poner un string en minusculas o mayuculas

minuscula = "vamos a gritar un poco"
grito = minuscula.upper()

mayuscula = "HABLEMOS MAS BAJITO"
susurro = mayuscula.lower()

#Comprobar si un string tiene prefijos o sufijos
url = "www.dota.com"
prefijo = url.startswith("www")
sufijo = url.endswith(".com")

print(prefijo)
print(sufijo)

#Encontrar la posiciòn del primer caràcter de la primera apariciòn del string sub en el string original, sì no lo encuentra devuelve -1

indice = url.find("dota")
print(indice)

#Concatenaciòn de strings y f-strings

nombre = "Isaias"
edad = 21
cargo = "Data Engineer"

saludo = "Mi nombre es " + nombre + " tengo una edad de " + str(edad) + " años y soy " + cargo 
saludo_2 = f"Mi nombre es {nombre} tengo una edad de {str(edad)} años y soy {cargo}"
print(saludo)
print(saludo_2)