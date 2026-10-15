import math

def bolzano(funcion, a, b):
    if funcion(a) * funcion(b) < 0:
        return True
    else:
        return False

def valor_medio(a, b):
    return (a + b) / 2

def biseccion(funcion, a, b, tolerancia, max_iteraciones):
    if not bolzano(funcion, a, b):
        raise Exception("No cumple el teorema de Bolzano")
    
    iteracion = 0
    while iteracion < max_iteraciones:
        c = valor_medio(a, b)

        if bolzano(funcion, a, c):
            b = c
        else:
            a = c

        if abs(funcion(c)) < tolerancia:
            return c

        iteracion += 1

    raise Exception("No se llego a una solucion dentro del numero maximo de itraciones")

if __name__ == "__main__":
    funcion = lambda x: math.cos(x) - x
    a = 0
    b = 1
    tolerancia = 1e-6   
    max_iteraciones = 100
    resultado = biseccion(funcion, a, b, tolerancia, max_iteraciones)
    print(f"Resultado: {resultado}")