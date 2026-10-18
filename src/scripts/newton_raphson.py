import sympy as sp

def derivar(funcion): #derivada
    x = sp.symbols('x')
    derivada = sp.diff(funcion(x), x)
    return derivada

def siguiente_punto(funcion, derivada, x_actual): #formula
    x_nueva = x_actual - (funcion(x_actual) / derivada.subs(sp.symbols('x'), x_actual))
    return x_nueva

def newton_raphson(funcion, x_actual, tolerancia, max_iteraciones): #paso iteratico
    iteracion = 0
    derivada = derivar(funcion)
    errores = []

    while iteracion < max_iteraciones:
        x_nueva = float(siguiente_punto(funcion, derivada, x_actual))
        error = abs((x_nueva - x_actual) / x_nueva) * 100 if x_nueva != 0 else abs(x_nueva - x_actual) * 100
        errores.append(error)
        if error < tolerancia:
            return x_actual, errores, iteracion

        x_actual = x_nueva
        iteracion += 1
    return None, "No se llego a una solucion dentro del numero maximo de itraciones"