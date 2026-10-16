import sympy as sp

def derivar(funcion, orden): #Calcular derivada
    x = sp.symbols('x')
    derivada = sp.diff(funcion(x), x, orden)
    return derivada

def siguiente_punto(funcion, derivada, segunda_derivada, x_actual): #Formula
    evaluacion_derivada = float(derivada.subs(sp.symbols('x'), x_actual))
    evaluacion_segunda_derivada = float(segunda_derivada.subs(sp.symbols('x'), x_actual))
    numerador = funcion(x_actual) * evaluacion_derivada
    denominador = (evaluacion_derivada**2) - funcion(x_actual) * evaluacion_segunda_derivada
    x_nueva = x_actual - (numerador / denominador)
    return x_nueva

def newton_raphson_modificado(funcion, x_actual, tolerancia, max_iteraciones): #Paso iterativo
    iteracion = 0
    derivada = derivar(funcion, 1)
    segunda_derivada = derivar(funcion, 2)

    while iteracion < max_iteraciones:
        x_nueva = siguiente_punto(funcion, derivada, segunda_derivada, x_actual)
        error = abs((x_nueva - x_actual) / x_nueva) * 100 if x_nueva != 0 else abs(x_nueva - x_actual) * 100
        x_actual = x_nueva

        if abs(funcion(x_actual)) < tolerancia:
            return x_actual, error, iteracion
        
        iteracion += 1

    return None, "No se llego a una solucion dentro del numero maximo de itraciones"