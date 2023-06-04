

def busquedaLineal(dato):
    for x in range(len(lista)):
        if lista[x] == dato:
            return x
    return None

def buscar(dato):
    if busquedaLineal(dato) is None:
        return "El dato %d no se encontró" % dato
    else:
        return "El dato %d se encontró en el índice: %d" % (dato, busquedaLineal(dato))

lista = [12, 45, 75, 9, 6, 5, 4, 2, 1, 0, 12, 45, 78, 63, 25, 98]


for i in range(len(lista)):
    print("[%d] => [%d]"%(i, lista[i]))



print(buscar(100))


