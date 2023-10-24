##BUCLES FOR IN ##
#Sintaxis:
# Acciones

numeros = list(range(0,77))
numeros_copia = []

for numero in numeros:
    numeros_copia.append(numero+1)
print(numeros_copia)

lista_palabras = ['Linkedin','Facebook','TikTok']

for palabra in lista_palabras:
    print(palabra)

##BUCLES WHILE ##
#Sintaxis:
# Acciones

suma = 1
while suma > 0:
    suma = suma - 1 
    print(suma)

## SENTENCIAS BREAK, PASS Y CONTINUE ##
#BREAK: Detiene la ejecucion del bucle

suma = 50

while suma > 0:
    suma = suma - 1
    print(suma)
    if suma == 20:
        break   

#PASS: Se utiliza para dejar vacio un trozo de codigo que todavia no queramos especificar

numeros = list(range(0,1000))

for numero in numeros:
    pass
print("test")

#Continue: Pasa a la siguiente iterasacion del bucle 
suma = 50

while suma > 0:
    suma = suma - 1
    if suma % 2 != 0:
        continue
    else:
        print(sum)



