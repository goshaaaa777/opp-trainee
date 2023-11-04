

dinero = float(input("Hola, indique el dinero que gastara. \n "))
DINERO_INICIAL = dinero

total = 0
pedido = []


margarita = 7.85
jamon_queso = 9.65
cuatro_quesos = 8.99
americana = 8.99
hawaiana = 7.90

extra_queso = 1.25
champinones = 0,85
albahaca = 1.15
jamon = 2.15

print("-> Pizzeria GoshA <-\n")

while True:
    print(f"1 - Margarita - {margarita}$")
    print(f"2 - Jamòn y queso - {jamon_queso}$")
    print(f"3 - cuatro quesos - {cuatro_quesos}$")
    print(f"4 - Americana - {americana}$")
    print(f"5 - Hawaiana - {hawaiana}$")

    eleccion = int(input("Hola, por favor, selecciona una pizza "))

    match eleccion:
        case 1:
            print(f"Ha elegido la pizza margarita.\nTotal a pagar {margarita}$")
            dinero -= margarita
            print(f"Le queda {round(dinero,2)}$")
            total += margarita
            pedido.append(f"Margarita - {margarita}$")
            break
        case 2:
            print(f"Ha elegido la pizza Jamòn y queso.\nTotal a pagar {jamon_queso}$")
            dinero -= jamon_queso
            print(f"Le queda {round(dinero,2)}$")
            total += jamon_queso
            pedido.append(f"Jamòn y queso - {jamon_queso}$")
            break
        case 3:
            print(f"Ha elegido la pizza Cuatro quesos.\nTotal a pagar {cuatro_quesos}$")
            dinero -= cuatro_quesos
            print(f"Le queda {round(dinero,2)}$")
            total += cuatro_quesos
            pedido.append(f"Cuatro Quesos - {cuatro_quesos}$")
            break
        case 4:
            print(f"Ha elegido la pizza americana.\nTotal a pagar {americana}$")
            dinero -= americana
            print(f"Le queda {round(dinero,2)}$")
            total += americana
            pedido.append(f"Americana - {americana}$")
            break
        case 5:
            print(f"Ha elegido la pizza hawaiana.\nTotal a pagar {hawaiana}$")
            dinero -= hawaiana
            print(f"Le queda {round(dinero,2)}$")
            total += hawaiana
            pedido.append(f"hawaiana - {hawaiana}$")
            break
        case _:
            print(f"Opcion incorrecta. Seleccione una opcion del 1 al 5")

    while True:
        print(f"1 - Extra de queso - {extra_queso}")
        print(f"2 - Champiñones - {champinones}")
        print(f"3 - Albahaca - {albahaca}")
        print(f"4 - Jamon - {jamon}")
        print(f"5 - No añadir nada extray pagar.")

        eleccion = int(input("Si desea algùn ingrediente extra.\n"))

        match eleccion:
            case 1:
                print(f"Ha elegido extra de queso.\n Extra a pagar {extra_queso}$")
                dinero -= extra_queso
                total += extra_queso
                print(f"Total a pagar: {total}$")
                print(f"Le queda {round(dinero,2)}$")
                pedido.append(f"Extra de queso - {extra_queso}$")
            case 2:
                print(f"Ha elegido extra de champinones.\n Extra a pagar {champinones}$")
                dinero -= champinones
                total += champinones
                print(f"Total a pagar: {total}$")
                print(f"Le queda {round(dinero,2)}$")
                pedido.append(f"Extra de champinones - {champinones}$")
            case 3:
                print(f"Ha elegido extra de albahaca.\n Extra a pagar {albahaca}$")
                dinero -= albahaca
                total += albahaca
                print(f"Total a pagar: {total}$")
                print(f"Le queda {round(dinero,2)}$")
                pedido.append(f"Extra de albahaca - {albahaca}$")
            case 4:
                print(f"Ha elegido extra de jamon.\n Extra a pagar {jamon}$")
                dinero -= jamon
                total += jamon
                print(f"Total a pagar: {total}$")
                print(f"Le queda {round(dinero,2)}$")
                pedido.append(f"Extra de jamon - {jamon}$")
            case 5:
                print("De acuerdo, no se añadio nada extra.")       
                break
            case _:
                print(f"Opcion incorrectoa. Selecicone una opcion 1 al 5.")
    
    if total <= DINERO_INICIAL:
        print("\n --- SU PEDIDO ---")
        print(f"El total de su pedido es {total}$")
        print(f"Su cambio: {dinero}$.\n")

        for i in pedido:
            print(f"-{i}.")

        print("\n!Buen provecho!")