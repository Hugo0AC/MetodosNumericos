def bolzano(funcion, a, b): #cambio signo
    if funcion(a) * funcion(b) < 0:
        return True
    else:
        return False

def valor_medio(a, b): #C
    return (a + b) / 2

def biseccion(funcion, a, b, tolerancia, max_iteraciones): #metodo iterativo
    if not bolzano(funcion, a, b):
        return None, "No cumple bolzano"

    iteracion = 0
    c_anterior = None 
    while iteracion < max_iteraciones:
        c = valor_medio(a, b)
        if c_anterior is not None:
            error = abs((c - c_anterior) / c) * 100 if c != 0 else abs(c - c_anterior) * 100
            if error < tolerancia:
                return c, error, iteracion       
        c_anterior = c 

        if bolzano(funcion, a, c):
            b = c
        else:
            a = c

        if abs(funcion(c)) < tolerancia: 
            return c, error, iteracion
        iteracion += 1

    return None, "No se llego a una solucion dentro del numero maximo de itraciones"