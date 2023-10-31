import utilidades

def formatear_texto(text:str, formato:str) -> str:
    if formato == 'minisculas':
        return utilidades.minisculas(text)
    elif formato == 'mayusculas':
        return utilidades.mayusculas(text)
    return f"El formato {formato} no existe."