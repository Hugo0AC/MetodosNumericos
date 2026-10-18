def bolzano(funcion, a, b): #cambio de signo
    if funcion(a) * funcion(b) < 0:
        return True
    else:
        return False

def punto_corte(funcion, a, b): #Nuevo punto C
    numerador = funcion(b) * (a - b)
    denominador = funcion(a) - funcion(b)
    c = b - (numerador / denominador)
    return c

def falsa_posicion(funcion, a, b, tolerancia, max_iteraciones): #iteracion
    if not bolzano(funcion, a, b):
        return None, "No cumple bolzano"
    iteracion = 0
    c_anterior = None
    errores = []
    
    while iteracion < max_iteraciones:
        c = punto_corte(funcion, float(a), float(b))
        if c_anterior is not None:
            error = abs((c - c_anterior) / c) * 100 if c != 0 else abs(c - c_anterior) * 100
            errores.append(error)
            if error < tolerancia:
                return c, errores, iteracion
        else:
            error = 0.0
        c_anterior = c

        if bolzano(funcion, float(a), float(c)):
            b = c
        else:
            a = c
        iteracion += 1

    return None, "No se llego a una solucion dentro del numero maximo de itraciones"